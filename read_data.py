import serial
import time
import json

import DB

def insert_serial(db, data):
    db["measurement"].insert_one(json.loads(data))

def read_serial(port, baudrate, db):
    try:
        ser = serial.Serial(port, baudrate)
        print(f'Connected to {port} at {baudrate} baudrate')

        while True:
            data = ser.readline().decode().strip()
            print('Received: ', data)
            insert_serial(db, data)

    except serial.SerialException as e:
        print("Serial connection error:", e)

def main():
    db = DB.connectToDB()
    db['measurement'].delete_many({})

    port = 'COM10'
    baudrate = 115200

    read_serial(port, baudrate, db)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()