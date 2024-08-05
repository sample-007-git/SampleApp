import requests

head = {
    'Accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",
                        headers=head,
                       verify=False)

print('before update:')
print(response.json())

head_PUT = {
'Accept': 'text/plain',
'Content-Type': 'application/json'
}

put_payload = {
    "id": 25,
    "title": "Salomon Joseph",
    "dueDate": "2024-08-04T13:54:52.903Z",
    "completed": True
}

responsePUT = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",
                        headers=head_PUT,
                           json=put_payload,
                        verify=False)

print('after update:')
print(responsePUT.json())

