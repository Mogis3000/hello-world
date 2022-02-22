import requests

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'nerdy'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
