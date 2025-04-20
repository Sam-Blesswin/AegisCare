# 🔐 AegisCare: Securing Microservices with CI/CD

AegisCare is a simulation platform designed to highlight vulnerabilities in CI/CD pipelines, microservices, and infrastructure-as-code setups. It integrates real-world security tools, attack simulations, and monitoring dashboards to generate build-time and runtime reports — forming the foundation for LLM-guided security fixes.

---

## 🚀 Current Features

### 🔧 Platform Stack
- **Backend**: FastAPI + PostgreSQL
- **Containerization**: Docker (multi-stage, non-root)
- **Infrastructure**: Terraform + Kubernetes (via kind)
- **CI/CD**: Jenkins (Docker agents)

### 🛡 Security & DevSecOps
- **Static Analysis**: SonarQube
- **Secrets Scanning**: Gitleaks
- **IaC Security**: Checkov
- **Image Scanning**: Trivy
- **Runtime Monitoring**: Prometheus + Grafana

### ⚔️ Simulated Vulnerabilities
- JWT forgery
- SQL Injection
- SSRF
- Open Redirects
- Resource Exhaustion (CPU, DB load)
- No input validation & weak auth

### 📄 Report Generation
- **Build Report**: logs from CI/CD tools and scanners
- **Runtime Report**: anomalies, pod metrics, attack effects, resource stats

---

## 📊 Dashboards
Built using **Grafana** with Prometheus metrics, showing:
- Pod CPU/memory usage
- API load and request anomalies
- DB access patterns
---

## 🎯 Future Goals: LLM-Driven Fixes
- Real-Time Context via MCP (Model Context Protocol)
- Integrate live feeds from OWASP, CVE databases, and latest tool release notes
- AI-Powered Code Review & Auto-Fix
- Suggests precise code or config fixes (line-by-line)
- Highlights all impacted files/paths
- Enables 1-click apply/discard workflow in PRs
- Goal: Fully Automated Secure CI/CD
---

## 📽️ Presentation

Check out the [Project Vision & Future Goals Slides](./reports/Aegiscare.pptx)

---