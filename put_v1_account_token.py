import requests

url = "http://localhost:5051/v1/account/3b192259-afca-47bd-a422-d9a5366d9730"

payload = {}
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
