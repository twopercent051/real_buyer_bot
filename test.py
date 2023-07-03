import requests
from requests.structures import CaseInsensitiveDict

url = "https://tglk.ru/in/5zJzjtgyEhkBaaa5"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"phonerb": "+79536305255"}'


resp = requests.post(url, headers=headers, data=data)

print(url, data, resp.content, sep="\n")
