variable "project_id" {
  description = "GCP project ID"
  type        = string
  default     = "gcp-gke-terraform-ci-cd"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-central2"
}

variable "cluster_name" {
  description = "GKE cluster name"
  type        = string
  default     = "gcp-devops-gke"
}

variable "network_name" {
  description = "VPC network name"
  type        = string
  default     = "gcp-devops-vpc"
}

variable "subnet_name" {
  description = "Subnet name"
  type        = string
  default     = "gcp-devops-subnet"
}