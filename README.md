Titanic API DevOps Platform
📌 Project Overview

This project demonstrates the end-to-end implementation of a production-ready cloud-native platform for the Titanic API. It integrates containerization, Kubernetes orchestration, CI/CD automation, observability, infrastructure automation, security hardening, and disaster recovery.

The platform is designed to ensure:

Scalabiliy and high availability

Security and compliance readiness

Operational visibility and monitoring

Automated deployment and recovery

🏗 Architecture & Tooling

Core Stack

Containerization: Docker

Orchestration: Kubernetes

Cloud: Amazon Web Services

Infrastructure as Code: Terraform

CI/CD: GitHub Actions

Monitoring: Prometheus

Visualization: Grafana

Logging: Grafana Loki

⚙️ DevOps Implementation

Part 1 — Containerization & Local Development

Dockerized Flask API

Docker Compose for local environment

Environment-based configuration

Result: consistent and portable development environment.

Part 2 — Kubernetes Deployment

Kubernetes manifests & overlays

Namespaces & service exposure

Resource management & scaling readiness

Result: scalable container orchestration.

Part 3 — CI/CD Pipeline

Automated build & testing

Image build & registry push

Kubernetes deployment automation

Result: continuous integration and delivery.

Part 4 — Observability & Monitoring

Metrics collection with Prometheus

Grafana dashboards

Centralized logging with Loki

Alerting for system health

Result: full system visibility and proactive alerting.

Part 5 — Infrastructure as Code

AWS infrastructure provisioning using Terraform

Remote state management

Environment separation & reproducibility

Result: version-controlled and repeatable infrastructure.

Part 6 — Security & Compliance

Kubernetes Network Policies

RBAC & least-privilege access

Secure secrets management practices

Container security considerations

Result: hardened and compliance-ready platform.

Part 7 — Disaster Recovery & Backup

Backup Strategy

Automated database backups

Retention & lifecycle policies

Point-in-time recovery capability

Kubernetes configuration backup

Disaster Recovery

RTO: 15 minutes

RPO: ≤ 5 minutes

Multi-AZ high availability

Failover procedures & recovery testing

Result: business continuity and rapid recovery.

🚀 Deployment Workflow

Developer pushes code

CI pipeline builds & tests

Container image is built & pushed

Kubernetes deployment updated

Monitoring & alerts track system health


💻 Local Development & API Setup
# titanic-api: Flask

Implemented using [Flask][] microframework.

## Installation and launching

### Clone

Clone the repo:

``` bash
git clone https://github.com/PipeOpsHQ/titanic-api.git
cd titanic-api
```

### Install

Use [venv][] or any other ([Pipenv][], [Poetry][], etc) [environment management][] tool to install dependencies in the same folder.
Activate virtual environment and run:

``` bash
pip install -r requirements.txt
```

### Launch

This API was tested using postgres. In order to bring it up, the following commands are needed:

1) Start postgres locally with `docker run --net=host --name titanic-db -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user -d postgres`
3) Run the sql file with the database definition `docker cp titanic.sql titanic-db:/`
4) Run the sql file with `docker exec -it --rm titanic-db psql -U user -d postgres -f titanic.sql`


After you have database server deployed and running, use environment variable `DATABASE_URL` to provide database connection string.

``` bash
DATABASE_URL=postgresql+psycopg2://user:password@127.0.0.1:5432/postgres python run.py
```

Go to <http://127.0.0.1:5000/> in your browser.

Test it by:
1) See the database is currently empty with: `http://127.0.0.1:5000/people`
2) Add a new user with `curl -H "Content-Type: application/json" -X POST localhost:5000/people -d'{"survived": 2,"passengerClass": 2,"name": "Mr. Owen Harris Braund","sex": "male","age": 22.0,"siblingsOrSpousesAboard": 4,"parentsOrChildrenAboard": 5,"fare": 7.25}`
3) Check out if the user was added with `http://127.0.0.1:5000/people`

[Flask]: http://flask.pocoo.org/
[venv]: https://docs.python.org/3/tutorial/venv.html
[Pipenv]: https://pipenv.pypa.io/en/latest/
[Poetry]: https://python-poetry.org/docs/
[environment management]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
