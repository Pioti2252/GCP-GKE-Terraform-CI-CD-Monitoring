output "cluster_name" {
  description = "GKE cluster name"
  value       = google_container_cluster.main.name
}

output "cluster_location" {
  description = "GKE cluster location"
  value       = google_container_cluster.main.location
}

output "network_name" {
  description = "VPC network name"
  value       = google_compute_network.main.name
}

output "subnet_name" {
  description = "Subnet name"
  value       = google_compute_subnetwork.main.name
}