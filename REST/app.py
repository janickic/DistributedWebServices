from flask import Flask
from flask_restful import Api, Resource, reqparse
import time, getip
app = Flask(__name__)
api = Api(app)

class timeNow(Resource):
    # Function for GET requests
    def get(self):
        now = time.time()
        # Create JSON response
        currTime = [
            {
                "time" : now
            }
        ]
        print("Server time: ", now)
        # Return JSON response with HTTP code 200
        return currTime[0], 200

# Create endpoint for timeNow class
api.add_resource(timeNow, "/time")

ip = getip.get()
# Expose server to the network
app.run(host='0.0.0.0')