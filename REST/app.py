from flask import Flask
from flask_restful import Api, Resource, reqparse
import time
app = Flask(__name__)
api = Api(app)


class timeNow(Resource):
    def get(self):
        now = time.time()
        currTime = [
            {
                "time" : str(now)
            }
        ]
        print "Server time: ", now
        return currTime[0], 200

api.add_resource(timeNow, "/time")

app.run(debug=True)
