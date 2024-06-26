import os
import sys
import time
import adafruit_dht
import board
import shutil

def GetTimestamp():
    """Get the current timestamp in Unix format (milliseconds)."""
    return int(time.time() * 1000)

def WriteTxtFile(name, device):
    current_directory = os.getcwd()
    if os.path.basename(current_directory) != "logger":
        os.chdir("logger")
    
    temperature, humidity = GetValuesFromDevice(device)
    if temperature==-404 and humidity==-404:
        return
    timestamp = GetTimestamp()
    
    file_path = f"./logs/{name}.txt"
    print(f"Using file {file_path}")
    
    line_to_write = f"{timestamp}:{name}:{temperature};{humidity}\n"
    print(f"Timestamp: {timestamp} -> Device {name} : T={temperature}°C | H={humidity}%")
    
    with open(file_path, 'a') as file:
        # Write the content to the file
        file.write(line_to_write)
        
def GetValuesFromDevice(device):
    try:
        temperature_c = device.temperature
        humidity = device.humidity
    except RuntimeError as err:
        print(err)
        temperature_c = -404
        humidity = -404
    
    return temperature_c, humidity

def backup_logs():
    current_directory = os.getcwd()
    if os.path.basename(current_directory) != "logger":
        os.chdir("logger")
    
    # Create a backup folder if it doesn't exist
    backup_dir = "./logs/backups"
    os.makedirs(backup_dir, exist_ok=True)

    # Generate timestamp for the backup file
    timestamp = GetTimestamp()
    backup_file_prefix = f"backup_{timestamp}"
    
    # Iterate over each log file and copy it to backups with timestamp
    for name in ["cooler", "darkbox", "outside"]:
        log_file = f"./logs/{name}.txt"
        backup_file = f"{backup_dir}/{backup_file_prefix}_{name}.txt"
        try:
            shutil.copy(log_file, backup_file)
            os.remove(log_file)
        except FileNotFoundError as err:
            print(err)
        print(f"Backup created: {backup_file}")

def main():
    current_directory = os.getcwd()
    if os.path.basename(current_directory) != "logger":
        os.chdir("logger")
    os.makedirs("logs", exist_ok=True)
    if os.path.exists("logs/cooler.txt") or os.path.exists("logs/darkbox.txt") or os.path.exists("logs/outside.txt"):
        backup_logs()
    
    #Define devices
    dht_device_cooler = adafruit_dht.DHT22(board.D17)
    dht_device_darkbox = adafruit_dht.DHT22(board.D27)
    dht_device_outside = adafruit_dht.DHT22(board.D22)
    devices = [dht_device_cooler,dht_device_darkbox,dht_device_outside]
    names = ["cooler","darkbox","outside"]  
            
    while True:
        for name,device in zip(names,devices):
            WriteTxtFile(name, device)
        time.sleep(10)

if __name__ == "__main__":
    main()
