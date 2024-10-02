import requests

url = 'https://ahi-dummy-test-2024.azurewebsites.net/api/hants_test?'

body = {
    "name": "Hants"
}

response = requests.post(url, json=body)

print(response.text)