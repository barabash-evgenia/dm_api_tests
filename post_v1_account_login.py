import requests
import json

url = "http://localhost:5051/v1/account/login"

payload = json.dumps({
  "login": "login_114",
  "password": "login_114",
  "rememberMe": False
})
headers = {
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
