# Data for assume role policy
data "aws_iam_policy_document" "irsa_assume" {
  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]

    principals {
      type        = "Federated"
      identifiers = [var.oidc_provider_arn]  # from EKS cluster
    }

    condition {
      test     = "StringEquals"
      variable = "${var.oidc_provider_url}:sub"
      values   = ["system:serviceaccount:${var.namespace}:${var.sa_name}"]
    }
  }
}

# IAM Role for the Service Account
resource "aws_iam_role" "irsa_role" {
  name               = "titanic-irsa-${var.sa_name}"
  assume_role_policy = data.aws_iam_policy_document.irsa_assume.json
}

# Attach a policy to the IRSA role
resource "aws_iam_role_policy_attachment" "irsa_policy_attach" {
  role       = aws_iam_role.irsa_role.name
  policy_arn = var.policy_arn
}

