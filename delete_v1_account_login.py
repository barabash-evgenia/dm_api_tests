import requests

url = "http://localhost:5051/v1/account/login"

payload = {}
headers = {
  'X-Dm-Auth-Token': 'IQJh+zgzF5ApLc2HuKVvD280AJa+svT3T8bZdE3e81TwBuSGSSl6TOHopbn4heMzsEpWx3SXbBZ15F2/ynMClqzh6DbalZCK3asu48xMTZMg8zOjZzfiTAEdIIgzKT2F2p2V9dpKEh8= ',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
