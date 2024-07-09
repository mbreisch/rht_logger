from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread
import requests
from time import sleep

import relay

app = Flask(__name__)

@app.route('/get_fan_control_data', methods=['GET'])
def get_fan_control_data():
    url = 'http://raspberrypisipm.am14.uni-tuebingen.de:5000/ambient/fan_control'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fan_control_data = response.json()
            return jsonify(success=True, data=fan_control_data)
        else:
            return jsonify({'error': f'Failed to fetch data. Status code: {response.status_code}'})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'})
    
def run_client():
    app.run(host='0.0.0.0', port=5001)
    
    while True:
        relay.fan_control_data = get_fan_control_data()
        sleep(1)