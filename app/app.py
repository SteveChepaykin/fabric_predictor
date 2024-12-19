from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import config
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.password
app.config['MYSQL_DB'] = config.database

mysql = MySQL(app)

@app.route('/add/<tagId>', methods=['POST'])
def add(tagId: int):
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO sensordata(tag, value, sourcetime) VALUES(%s, %s, %s)", 
                   (tagId, data['value'], data['sourcetime']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'new data from sensor added'}), 201

@app.route('/get/<tagId>', methods=['GET'])
def users(tagId: int):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM sensordata WHERE tag=%s", (tagId))
    results = list(map(__cast2map, cursor.fetchall()))
    cursor.close()
    return results

def __cast2map(ll: list) -> dict:
    r = {}
    r['tag'] = ll[0]
    r['value'] = ll[1]
    r['sourcetime'] = ll[2]
    return r

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    PORT = os.environ.get('SERVER_PORT', '5050')
    app.run(host=HOST, port=PORT, debug=True)