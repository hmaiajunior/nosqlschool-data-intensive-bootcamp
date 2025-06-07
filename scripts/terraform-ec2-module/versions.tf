# required_version indica a versão mínima do Terraform necessária.
# required_providers indica a versão do provider AWS que queremos utilizar.

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
