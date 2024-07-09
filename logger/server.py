from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread
import requests
from time import sleep

import relay
import rht

app = Flask(__name__)
CORS(app)

fan_status = {
    "relay": "OFF",
    "countdown": "30:00"
}

get_rht_status = {
    "cooler" : {"timestamp": "0","temperature": 0,"humidity": 0},
    "darkbox" : {"timestamp": "0","temperature": 0,"humidity": 0},
    "outside" : {"timestamp": "0","temperature": 0,"humidity": 0}
}

@app.route('/fan_status')
def get_fan_status():
    return jsonify(relay.status)

@app.route('/rht_status')
def get_rht_status():
    return jsonify(rht.status)

def run_client():
    while True:
        relay.fan_control_data = get_fan_control_data()
        sleep(1)

@app.route('/get_fan_control_data', methods=['GET'])
def get_fan_control_data():
    url = 'http://raspberrypisipm.am14.uni-tuebingen.de:5000/ambient/fan_control'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            relay.fan_control_data = response.json()
            return response.json()
        else:
            print(f'Failed to fetch data. Status code: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {str(e)}')
        return None

def run_flask():
    app.run(host='0.0.0.0', port=5000)
    
if __name__ == "__main__":
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()
        
        client_thread = Thread(target=run_client)
        client_thread.daemon = True
        client_thread.start()
        
        fan_thread = Thread(target=relay.run_relay)
        fan_thread.daemon = True
        fan_thread.start()
        
        rht_thread = Thread(target=rht.run_rht)
        rht_thread.daemon = True
        rht_thread.start()
        
        try:
            flask_thread.join()
            client_thread.join()
            fan_thread.join()
            rht_thread.join()
        except KeyboardInterrupt:
            print("Program interrupted.")