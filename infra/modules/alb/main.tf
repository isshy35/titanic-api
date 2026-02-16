resource "aws_lb" "app" {
  load_balancer_type = "application"
  subnets = module.vpc.public_subnets
}
