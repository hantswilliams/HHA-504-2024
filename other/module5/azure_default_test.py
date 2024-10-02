import requests 

url = "https://hants-serverless-test.azurewebsites.net/api/http_trigger1?code=RBncRZXOJAjF8U5i5RgVKr-NHuYulmwrEZVcVbypE3OPAzFuAhrjZQ%3D%3D"

body = {
    "name": "Hants Williams"
}

response = requests.post(url, json=body)

print(response.text)