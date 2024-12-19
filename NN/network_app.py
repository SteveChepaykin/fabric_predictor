import requests
import pandas as pd
import logging
import os

from flask import Flask, jsonify

app = Flask(__name__)

logger = logging.getLogger(__name__)

@app.route('/forecast', methods=['GET'])
def forecast():
    allframesX = []
    good = {1: 24, 2: 100, 3: 24}
    listkey = list(good.keys())
    isOk = True

    for tag in listkey:
        frame = requests.get("http://service_app:5050/get/{0}".format(tag)).json()
        allframesX.append(frame[-1])

    for i in range(len(good)):
        if(allframesX[i]["value"] != good[listkey[i]]):
            isOk = False
            break

    frameY = requests.get("http://service_app:5050/get/5").json()[-1];
    if frameY["value"] != 1:
        isOk = False;

    return jsonify({"status": "OK" if isOk else "BAD"});

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    PORT = os.environ.get('SERVER_PORT', '5055')
    app.run(host=HOST, port=PORT, debug=True)