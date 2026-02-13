module "iam" {
  source = "../../modules/iam"

  sa_name           = "my-service-account"
  namespace         = "default"
  oidc_provider_arn = module.eks.cluster_oidc_arn
  oidc_provider_url = module.eks.cluster_oidc_url
  policy_arn        = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}
