import requests 

url = 'https://us-central1-stony-brook-projects.cloudfunctions.net/blood-pressure'

body = {
    "systolic": 80.5,
    "diastolic": "100"
}

response = requests.post(url, json=body)

print(response.text)