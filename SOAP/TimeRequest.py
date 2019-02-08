# import the generated class stubs
from TimeServer_client import *
import sys, time

# Check IP of server
if len(sys.argv) < 2:
    print "Please insert IP of server"
    sys.exit()

ip = sys.argv[1]
print "Server ip: ", ip 

# Get a port proxy instance
loc  = TimeServerLocator()
# Find server location
port = loc.getTimeServer(url='http://'+ip+':7000/Time')
# Create new request
req = TimeRequest()
# Get time before remote call
start = time.time()
# Call the remote method
resp = port.Time(req)

# Get response value
serverTime = resp._value
# Calculate rtt
end = time.time()
rtt = (end - start) / 2
updatedTime = serverTime + rtt
# Print results
print "Server time:\t ", serverTime
print "RTT:\t\t ", rtt
print "Updated time:\t ", updatedTime