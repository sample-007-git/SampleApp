import requests

head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 23,
    "title": "Salomon E",
    "dueDate": "2024-08-04T13:29:47.355Z",
    "completed": True
}

response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Activities',
                         headers=head,
                         json=request_payload,
                         verify=False)

print(response.status_code)
print(response.json())

data = response.json()

assert response.status_code == 200
assert data['id'] == 23