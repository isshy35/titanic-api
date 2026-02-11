from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from pythonjsonlogger import jsonlogger
import logging
import time

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# =====================================================
# Structured JSON Logging Configuration
# =====================================================
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s"
)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# =====================================================
# Prometheus Metrics
# =====================================================
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency in seconds"
)

# =====================================================
# OpenTelemetry Tracing
# =====================================================
trace.set_tracer_provider(TracerProvider())

# Change the endpoint to your OTEL collector if not local
exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(exporter)
)

tracer = trace.get_tracer(__name__)

# =====================================================
# Flask App
# =====================================================
app = Flask(__name__)

# Instrument Flask app for automatic tracing
FlaskInstrumentor().instrument_app(app)

# =====================================================
# Middleware for Prometheus metrics
# =====================================================
@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def record_metrics(response):
    duration = time.time() - request.start_time

    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code
    ).inc()

    REQUEST_LATENCY.observe(duration)

    return response

# =====================================================
# Routes
# =====================================================
@app.route("/")
def home():
    logger.info("Root endpoint called")
    return jsonify(message="Titanic API is running")


@app.route("/health")
def health():
    logger.info("Health endpoint called")
    return jsonify(status="healthy", service="titanic-api")


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/predict")
def predict():
    # Example custom span for business logic
    with tracer.start_as_current_span("predict-span"):
        logger.info("Predict endpoint called")
        # Placeholder logic for prediction
        result = {"survived": True}
        return jsonify(result=result)

# =====================================================
# App start
# =====================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
