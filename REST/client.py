import requests, json, sys, time

if len(sys.argv) < 2:
    print("Please insert IP of server")
    sys.exit()

ip = sys.argv[1]
print('Server ip:', ip)
start = time.time()
response = requests.get("http://"+ip+":5000/time")
serverTime = response.json()["time"]
end = time.time()
rtt = (end - start) / 2
updatedTime = serverTime + rtt
print("Server time: ", serverTime)
print("Updated time: ", updatedTime)
