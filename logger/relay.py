import RPi.GPIO as GPIO
import time

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
        print(fan_control_data)
    print()

def cleanup():
    GPIO.cleanup()

def run_relay():
    try:
        setup_gpio(RELAY_PIN)
        while True:
            # Turn off for 30 minutes with countdown
            turn_off(RELAY_PIN)
            countdown(2)

            # Turn on for 5 minutes with countdown
            turn_on(RELAY_PIN)
            countdown(1)
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup()
        print("GPIO cleanup done.")
