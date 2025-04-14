import requests
from concurrent.futures import ThreadPoolExecutor

URL_DB = "http://127.0.0.1:8000/load/trade"
URL_COMPUTE = "http://127.0.0.1:8000/load/compute"


def hammer(url, label, count=50):
    def spam(i):
        try:
            r = requests.post(url, timeout=5)
            print(f"[{label} {i}] {r.status_code} - {r.json()}")
        except Exception as e:
            print(f"[{label} {i}] Failed: {e}")

    with ThreadPoolExecutor(max_workers=25) as executor:
        for i in range(count):
            executor.submit(spam, i)


if __name__ == "__main__":
    print("🚀 Starting DB-heavy flood...")
    hammer(URL_DB, "DB", count=100)

    print("🔥 Starting Compute-heavy flood...")
    hammer(URL_COMPUTE, "CPU", count=100)
