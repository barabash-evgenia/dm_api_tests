import requests
import json

url = "http://localhost:5051/v1/account/password"

payload = json.dumps({
  "login": "login_114",
  "token": "d39efcf3-8064-43cb-9df6-b878de4ab866",
  "oldPassword": "login_114",
  "newPassword": "login_444"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
