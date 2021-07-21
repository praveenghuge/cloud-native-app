import json
from flask import Flask
from flask import Response
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    ## log line
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    ## log line
    app.logger.info('Status request successfull')
    return Response(
    response=json.dumps({"result: OK - healthy"}),
    status=200,)

@app.route("/metrics")
def metrics():
    ## log line
    app.logger.info('Metrics request successfull')

    return Response(
    response=json.dumps({"UserCount": "140", "UserCountActive": "23"}),
    status=200,)


if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
