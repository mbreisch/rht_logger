import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
CORS(app)

RELAY_PIN = 26
status = {
    "relay": "OFF",
    "countdown": "30:00"
}

def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    status["relay"] = "ON"
    print(f"Relay on pin {pin} is now ON.")

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)
    status["relay"] = "OFF"
    print(f"Relay on pin {pin} is now OFF.")

def countdown(minutes):
    for remaining in range(minutes * 60, 0, -1):
        minutes_remaining = remaining // 60
        seconds_remaining = remaining % 60
        status["countdown"] = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(f"\rCountdown: {status['countdown']}", end="")
        time.sleep(1)
    print()

def cleanup():
    GPIO.cleanup()

@app.route('/status')
def get_status():
    return jsonify(status)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    try:
        setup_gpio(RELAY_PIN)
        
        # Start Flask server in a separate thread
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        print("Flask server is up and running...")

        while True:
            # Turn off for 30 minutes with countdown
            turn_off(RELAY_PIN)
            countdown(10)

            # Turn on for 5 minutes with countdown
            turn_on(RELAY_PIN)
            countdown(10)

    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup()
        print("GPIO cleanup done.")
import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

RELAY_PIN = 26
status = {
    "relay": "OFF",
    "countdown": "30:00"
}

def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    status["relay"] = "ON"
    print(f"Relay on pin {pin} is now ON.")

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)
    status["relay"] = "OFF"
    print(f"Relay on pin {pin} is now OFF.")

def countdown(minutes):
    for remaining in range(minutes * 60, 0, -1):
        minutes_remaining = remaining // 60
        seconds_remaining = remaining % 60
        status["countdown"] = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(f"\rCountdown: {status['countdown']}", end="")
        time.sleep(1)
    print()

def cleanup():
    GPIO.cleanup()

@app.route('/status')
def get_status():
    return jsonify(status)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    try:
        setup_gpio(RELAY_PIN)
        
        # Start Flask server in a separate thread
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        print("Flask server is up and running...")

        while True:
            # Turn off for 30 minutes with countdown
            turn_off(RELAY_PIN)
            countdown(30)

            # Turn on for 5 minutes with countdown
            turn_on(RELAY_PIN)
            countdown(5)

    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup()
        print("GPIO cleanup done.")
import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

RELAY_PIN = 26
status = {
    "relay": "OFF",
    "countdown": "30:00"
}

def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    status["relay"] = "ON"
    print(f"Relay on pin {pin} is now ON.")

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)
    status["relay"] = "OFF"
    print(f"Relay on pin {pin} is now OFF.")

def countdown(minutes):
    for remaining in range(minutes * 60, 0, -1):
        minutes_remaining = remaining // 60
        seconds_remaining = remaining % 60
        status["countdown"] = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(f"\rCountdown: {status['countdown']}", end="")
        time.sleep(1)
    print()

def cleanup():
    GPIO.cleanup()

@app.route('/status')
def get_status():
    return jsonify(status)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    try:
        setup_gpio(RELAY_PIN)
        
        # Start Flask server in a separate thread
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        print("Flask server is up and running...")

        while True:
            # Turn off for 30 minutes with countdown
            turn_off(RELAY_PIN)
            countdown(30)

            # Turn on for 5 minutes with countdown
            turn_on(RELAY_PIN)
            countdown(5)

    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup()
        print("GPIO cleanup done.")
