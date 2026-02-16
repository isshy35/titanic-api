module "eks" {
  source  = "terraform-aws-modules/eks/aws"

  cluster_name    = "titanic-eks"
  cluster_version = "1.29"

  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      min_size     = 2
      max_size     = 5
      desired_size = 2
      instance_types = ["t3.medium"]
    }
  }
}
