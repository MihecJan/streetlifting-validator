import serial
import time
import json

port = serial.Serial('COM10', 115200)

fake_data = {
    "timestamp": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    "gyroscope": {
        "x": [0.02, 0.03, 0.05, 0.08, 0.1, 0.12, 0.14, 0.15, 0.16, 0.17],
        "y": [-0.01, -0.02, -0.03, -0.04, -0.05, -0.06, -0.07, -0.08, -0.09, -0.1],
        "z": [0.03, 0.05, 0.08, 0.11, 0.14, 0.17, 0.2, 0.23, 0.26, 0.29]
    },
    "accelerometer": {
        "x": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "y": [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
        "z": [9.81, 9.82, 9.83, 9.84, 9.85, 9.86, 9.87, 9.88, 9.89, 9.9]
    }
}

ind = 0
while True:
    data = {
        "timestamp": fake_data["timestamp"][ind % len(fake_data["timestamp"])],
        "gyroscope": {
            "x": fake_data["gyroscope"]["x"][ind % len(fake_data["gyroscope"]["x"])],
            "y": fake_data["gyroscope"]["y"][ind % len(fake_data["gyroscope"]["y"])],
            "z": fake_data["gyroscope"]["z"][ind % len(fake_data["gyroscope"]["z"])]
        },
        "accelerometer": {
            "x": fake_data["accelerometer"]["x"][ind % len(fake_data["accelerometer"]["x"])],
            "y": fake_data["accelerometer"]["y"][ind % len(fake_data["accelerometer"]["y"])],
            "z": fake_data["accelerometer"]["z"][ind % len(fake_data["accelerometer"]["z"])]
        }
    }

    message = bytes((json.dumps(data) + "\n\r").encode("utf-8"))

    port.write(message)

    ind += 1
    time.sleep(1)