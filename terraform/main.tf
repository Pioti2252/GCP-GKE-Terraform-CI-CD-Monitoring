resource "google_compute_network" "main" {
  name                    = var.network_name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "main" {
  name          = var.subnet_name
  region        = var.region
  network       = google_compute_network.main.id
  ip_cidr_range = "10.10.0.0/24"
}

resource "google_container_cluster" "main" {
  name     = var.cluster_name
  location = var.region

  enable_autopilot = true

  network    = google_compute_network.main.id
  subnetwork = google_compute_subnetwork.main.id

  deletion_protection = false
}