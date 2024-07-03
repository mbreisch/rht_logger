from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

import relay
import rht

app = Flask(__name__)
CORS(app)

fan_status = {
    "relay": "OFF",
    "countdown": "30:00"
}

get_rht_status = {
    "timestamp": "0",
    "temperature": 0,
    "humidity": 0
}

@app.route('/status')
def get_fan_status():
    return jsonify(relay.status)

# @app.route('/rht_status')
# def get_rht_status():
#     return jsonify(rht.status)

def run_flask():
    app.run(host='0.0.0.0', port=5000)
    
if __name__ == "__main__":
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()
        
        fan_thread = Thread(target=relay.run_relay)
        fan_thread.daemon = True
        fan_thread.start()
        
        # rht_thread = Thread(target=rht.run_rht)
        # rht_thread.daemon = True
        # rht_thread.start()
        
        try:
            flask_thread.join()
            fan_thread.join()
            # rht_thread.join()
        except KeyboardInterrupt:
            print("Program interrupted.")