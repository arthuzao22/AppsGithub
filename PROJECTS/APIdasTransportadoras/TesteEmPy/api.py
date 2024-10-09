import requests

url = "https://tracking-apigateway.rte.com.br/token"

payload = {
    "auth_type": "DEV",
    "grant_type": "password",
    "username": "25370117000198",
    "password": "CDG102030"
}
headers = {"content-type": "application/x-www-form-urlencoded"}

response = requests.post(url, data=payload, headers=headers)

print(response.text)