from flask import Flask, render_template, request, make_response, g
import os
import socket
import random
import json
import logging

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)



@app.route("/", methods=['POST','GET'])
def hello():
    return '<h1>Bonjour tout le monde</h1>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
