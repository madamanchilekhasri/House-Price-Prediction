# Terraform / AWS (optional)
This starter demonstrates an artifact bucket only. It does not deploy the application or configure IAM.
Before use: configure AWS credentials, review the Terraform plan and expected costs, and never commit credentials.
Run `terraform init`, `terraform plan`, then `terraform apply` only if you understand the resources being created.
The configuration uses `random_id`; add the `hashicorp/random` provider to `required_providers` before applying.
