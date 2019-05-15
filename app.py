import time
from flask import Flask
import platform

host = platform.node()
app = Flask(__name__)

@app.route('/')
def hello():
    s = 'Hello World! I am <b>{}</b>!\n'.format(host)
    return s

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)