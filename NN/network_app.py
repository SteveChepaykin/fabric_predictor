import requests
import pandas as pd
import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/forecast', methods=['GET'])
def forecast():
    allframesX = [];

    # for tag in [1, 2, 4, 5, 7]:
    #     frame = pd.DataFrame(requests.get("http://localhost:5050/get/{0}".format(tag)));
    #     allframesX.add(frame)

    # frameY = pd.DataFrame(requests.get("http://localhost:5050/get/10"));

    # result = allframesX[0]
    # for i in range(1, len(allframesX)):
    #     result =  result.merge(allframesX[i], on='source_time', how='inner', suffixes=(i, i + 1))
    # frameX = result.index
    # for c in result.columns:
    #     if c.startswith("value"):
    #         frameX[c] = result[c]

    # for i in range(5):
    #     index = frameX.iloc[1:,:]
    
    # print(frameX)
    # print(frameY)

    return jsonify({"status": "OK"})

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    PORT = os.environ.get('SERVER_PORT', '5050')
    app.run(host=HOST, port=PORT, debug=True)