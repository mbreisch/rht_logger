import RPi.GPIO as GPIO
import time
from time import sleep

RELAY_PIN = 26
status = {
    "relay": "OFF",
    "countdown": "30:00"
}

fan_control_data = {"mode": "null","offTime": -1,"onTime": -1,"state": -1}

def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def turn_on(pin):
    if status.get("relay") != "ON":
        GPIO.output(pin, GPIO.HIGH)
        status["relay"] = "ON"
        print(f"Relay on pin {pin} is now ON.")

def turn_off(pin):
    if status.get("relay") != "OFF":
        GPIO.output(pin, GPIO.LOW)
        status["relay"] = "OFF"
        print(f"Relay on pin {pin} is now OFF.")


def countdown(minutes):
    for remaining in range(minutes * 60, 0, -1):
        if fan_control_data.get("mode") == "manual":
                break
        minutes_remaining = remaining // 60
        seconds_remaining = remaining % 60
        status["countdown"] = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(f"\rCountdown: {status['countdown']} ", end="")
        time.sleep(1)
        print(fan_control_data)
    print()

def cleanup():
    GPIO.cleanup()

def run_relay():
    try:
        setup_gpio(RELAY_PIN)
        while True:
            if fan_control_data.get("mode") == "manual":
                    if fan_control_data.get("state") == 1:
                        turn_on(RELAY_PIN)
                    else:
                        turn_off(RELAY_PIN)
                    sleep(1)
            elif fan_control_data.get("mode") == "auto":
                while True:
                    turn_off(RELAY_PIN)
                    countdown(int(fan_control_data.get("offTime")))
                    if fan_control_data.get("mode") == "manual":
                        break

                    turn_on(RELAY_PIN)
                    countdown(int(fan_control_data.get("onTime")))
                    if fan_control_data.get("mode") == "manual":
                        break
            else:
                sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup()
        print("GPIO cleanup done.")
