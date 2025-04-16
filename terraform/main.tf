terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.20.0"
    }
  }
}

provider "kubernetes" {
  config_path    = "/root/.kube/config"
  config_context = "kind-aegiscare"
  insecure       = true # Set to true for insecure connections #local CI/CD to work in docker
}

resource "kubernetes_namespace" "staging" {
  metadata {
    name = "staging"
  }
}

resource "kubernetes_secret" "db_secret" {
  metadata {
    name      = "db-secrets"
    namespace = kubernetes_namespace.staging.metadata[0].name
  }

  data = {
    DB_USER     = base64encode("vulnuser")
    DB_PASSWORD = base64encode("vulnpass")
    DB_NAME     = base64encode("finsec")
  }

  type = "Opaque"
}
