# import the generated class stubs
from TimeServer_client import *
import sys, time

if len(sys.argv) < 2:
    print "Please insert IP of server"
    sys.exit()

ip = sys.argv[1]
print 'Server ip:', ip


# get a port proxy instance
loc  = TimeServerLocator()
port = loc.getTimeServer(url='http://'+ip+':7000/Time')

# create new request
req = TimeRequest()
# call the remote method
resp = port.Time(req)
# print the resulting quotation
print resp._value
print "Current time on Server: ", resp._value
