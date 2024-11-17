from flask import Flask
import os
import time

app = Flask(__name__)

# Initialize a start time for uptime calculation
start_time = time.time()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status')
def status():
    uptime = time.time() - start_time
    return {
        "status": "running",
        "uptime_seconds": int(uptime),
        "version": "1.0.0"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
