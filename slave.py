import requests
import json

res = requests.get("https://twitch-python.vercel.app/get_my_ip")
response = json.loads(res.text)
print(response)
