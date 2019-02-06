import requests, json, sys

if len(sys.argv) < 2:
    print "Please insert IP of server"
    sys.exit()

ip = sys.argv[1]
print 'Server ip:', ip

response = requests.get("http://"+ip+":5000/time")
serverTime = response.json()
print "Server time: ", serverTime["time"]
