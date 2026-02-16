module "db" {
  source  = "terraform-aws-modules/rds/aws"

  identifier = "titanic-db"

  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"

  allocated_storage    = 20

  subnet_ids           = module.vpc.private_subnets
  multi_az             = true
  backup_retention_period = 7

  publicly_accessible = false
}
