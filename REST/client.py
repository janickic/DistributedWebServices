import requests, json, sys, time

# Check IP of server
if len(sys.argv) < 2:
    print("Please insert IP of server")
    sys.exit()
ip = sys.argv[1]
print('Server ip:', ip)

# Get time before remote call
start = time.time()
# Call the remote server
response = requests.get("http://"+ip+":5000/time")
# Parse out JSON reponse
serverTime = response.json()["time"]
# Get time after remote call
end = time.time()
# Calculate rtt
rtt = (end - start) / 2
updatedTime = serverTime + rtt
# Output results
print("Server time: ", serverTime)
print("Updated time: ", updatedTime)
