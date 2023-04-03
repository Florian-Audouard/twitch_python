import requests
import json

res = requests.get("https://twitch-python.vercel.app/getget_my_ip")
response = json.loads(res.ip)
