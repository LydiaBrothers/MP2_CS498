from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

# Route for handling HTTP POST request
@app.route('/', methods=['POST'])
def stress_cpu():
    # Create a separate process to run "stress_cpu.py"
    subprocess.Popen(['python', 'stress_cpu.py'])
    return "Stressing CPU in a separate process."

# Route for handling HTTP GET request
@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
