import datetime

def log_sensor_reading(sensor_name, reading):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp}: {sensor_name} reading: {reading}")

# Example usage:
log_sensor_reading("Temperature", 25)
