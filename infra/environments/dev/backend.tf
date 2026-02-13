terraform {
  backend "s3" {
    bucket       = "titanic-terraform-state2026"
    key          = "dev/terraform.tfstate"
    region       = "us-east-2"
    encrypt      = true
    use_lockfile = true   # replaces dynamodb_table
  }
}
