"""Main application file"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! <h1>HELLO THERE SUNSHINE!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
