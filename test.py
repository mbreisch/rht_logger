import time
import adafruit_dht
import board

dht_device_0 = adafruit_dht.DHT22(board.D17)
dht_device_1 = adafruit_dht.DHT22(board.D27)
dht_device_2 = adafruit_dht.DHT22(board.D22)

devices = [dht_device_0,dht_device_2,dht_device_2]

while True:
    try:
        for enum,device in enumerate(devices):
            temperature_c = device.temperature
            temperature_f = temperature_c * (9 / 5) + 32

            humidity = device.humidity

            print(f"D{enum}: Temp:{temperature_c} C / {temperature_f} F / Humidity: {humidity}%")
            time.sleep(2.0)
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(2.0)