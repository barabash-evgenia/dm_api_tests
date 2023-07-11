import requests

url = "http://localhost:5051/v1/account/login/all"

payload = {}
headers = {
  'X-Dm-Auth-Token': 'IQJh+zgzF5DVFTHleUBks5KWy6yRimiinhDWnGthBkA1FcfFCjNoyqvKRNrKLXRUdnHrTfTEE3edbH8gy1tDqScSzXzNCNYLAbW5FjZWH/A1n8ZU0+VacHfbJU/ThyrkwaUp+krkiMA=',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
