import os 
from __init__ import logger

# os.chdir('..')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.info('Hello World !!!!!!!!!')
    return 'Hello, World! (from a Docker container)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
