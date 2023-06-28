import requests
from requests.structures import CaseInsensitiveDict

url = "https://webhook.site/dc1beebb-ae1c-4934-aa6f-b1a4a7c8cb0e"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"phonerb": "+79536305255"}'


resp = requests.post(url, headers=headers, data=data)

print(url, data, resp.content, sep="\n")
