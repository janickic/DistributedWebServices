import requests, json

response = requests.get("http://127.0.0.1:5000/time")
serverTime = response.json()
print "Server time: ", serverTime["time"]
