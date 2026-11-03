# Optional AWS starter. Review costs, region, security and credentials before applying.
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}
variable "aws_region" { type = string, default = "ap-south-1" }
provider "aws" { region = var.aws_region }

# This creates a small S3 bucket for artifacts; it does NOT deploy the app.
resource "random_id" "suffix" { byte_length = 4 }
resource "aws_s3_bucket" "artifacts" {
  bucket = "house-price-mlops-artifacts-${random_id.suffix.hex}"
  force_destroy = false
  tags = { Project = "house-price-prediction-mlops" }
}
