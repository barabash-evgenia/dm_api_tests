import requests
import json

url = "http://localhost:5051/v1/account/password"

payload = json.dumps({
  "login": "login_112",
  "email": "login_112@mail.ru"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
