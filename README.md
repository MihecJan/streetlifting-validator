# Streetlifting validator

**simulate_data.py:** This script generates fake data and sends it to the virtual serial port COM10.

**read_data.py:** Reads the fake data from the COM10 port and stores it in a MongoDB database. (The database is cleared each time the script starts)

**server.py:** This script serves the index.html file and transmits measurement data to clients via a WebSocket connection.

## Get started
1. **Create and start virtual serial port COM10:** 
    - Download and install VSPE eterlogic (4 weeks free trial available).
    - Launch VSPE and click on create a new device:
        - Device type: Connector
        - Select COM10
        - Check emulate baud rate
        - Complete the setup process.

2. **MongoDB setup:**
    - Install MongoDB if you haven't already.
    - Create a new database named "streetliftingValidatorDB".
    - Within the database, create a collection named "measurement".

3. **Run simulate_data.py:**
    - Execute this script to generate fake data. Keep it running while testing.

4. **run server.py:**
    - Start the server which serves the index.html file and handles WebSocket connections.
    - The server automatically detects changes. Keep it running.

5. **Access the web interface:**
    - Open your web browser and navigate to http://127.0.0.1:5000/ to access the application interface.

6. **Run read_data.py**
    - Execute this script to read data from the virtual serial port and store it in the MongoDB database.
    - Stop the script to halt data ingestion.
    - Re-run the script to clear existing measurements in the database and start afresh.