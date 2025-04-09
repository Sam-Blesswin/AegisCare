# AegisCare

A hands-on project to simulate **real-world CI/CD pipeline flaws**, **API vulnerabilities**, and **infrastructure misconfigurations** in a FastAPI-based FinTech app. Includes full DevSecOps stack: Docker, Kubernetes, Jenkins, Terraform, Prometheus, and Grafana.

---

## 📦 Project Structure

```
ci-cdguard-finsec/
├── backend/          # FastAPI app with JWT, DB, endpoints
├── terraform/        # Infrastructure as Code for Jenkins + App
├── jenkins/          # Jenkinsfiles (secure + vulnerable)
├── k8s/              # K8s manifests: deployments, services, HPA
├── monitoring/       # Prometheus & Grafana configs
├── attacks/          # Attack scripts (SQLi, JWT, XSS, etc.)
├── docker/           # Docker compose to start additional service (eg: postgres)
└── README.md
```

---

## 🎯 Use Case

- Learn & practice DevSecOps with FastAPI
- Simulate **vulnerable CI/CD pipeline**
- Inject and fix **critical security issues**
- Visualize metrics via **Grafana**
- Compare secure vs insecure deployments

---

## 🧪 Vulnerabilities Simulated

- SQL Injection
- JWT Forgery
- Rate Limit Bypass
- CORS Misconfig
- CSRF
- Open Redirect
- SSRF
- XSS

---

## 🔐 Tech Stack

- **FastAPI** — Backend API (FinTech/Asset management theme)
- **Jenkins** — CI/CD pipelines
- **Docker** — Multi-stage secure images
- **Kubernetes (Minikube)** — App deployment + HPA
- **Terraform** — Infra provisioning
- **Prometheus + Grafana** — Monitoring & dashboards

---

## 🚀 Getting Started

```bash
# Clone repo and enter project
git clone https://github.com/Sam-Blesswin/AegisCare.git
cd AegisCare

# Setup FastAPI backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

---

## 📌 Branching Strategy

| Branch       | Purpose                            |
|--------------|------------------------------------|
| `main`       | Final secure version               |
| `vuln-demo`  | Insecure version with flaws        |
| `secure-demo`| Hardened version for comparison    |
| `dev`        | Active development branch          |

---