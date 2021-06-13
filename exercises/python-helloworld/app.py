## Solution for endpoints obtained through Udacity

from flask import Flask
from flask import json
import logging

app = Flask(__name__)

FORMAT = '%(asctime)s, %(funcName)s %(message)s'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format = FORMAT)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result" : "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    logging.debug('endpoint was reached')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({
            "status" : "success",
            "code" : 0,
            "data" : {"UserCount" : 140, "UserCountActive": 23}
        }),
        status=200,
        mimetype='application/json'
        )
    logging.debug('endpoint was reached')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')