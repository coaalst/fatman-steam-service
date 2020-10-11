from flask import send_file
from app import app

import json, os

# Make and send screenshot
@app.route('/', methods=['GET'])
def send_image():

    basedir = os.path.abspath(os.path.dirname(__file__))
    os.system('fswebcam -r 1024x768 -S 10 ' + os.path.join(basedir, 'vladanaa.jpg'))

    filename = 'vladanaa.jpg'
    return send_file(filename, mimetype='image/jpg')