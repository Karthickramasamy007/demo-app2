from flask import Flask
app = Flask(__name__)

@app.route('/app2')
def hello_world():
    return 'Hello, This is demo app2'