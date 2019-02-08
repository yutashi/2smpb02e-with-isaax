# coding: utf-8
# Sample that outputs the value acquired by 2SMPD-02E.

from __future__ import print_function

import time
import datetime
from flask import Flask
from flask import render_template
from flask import jsonify

import grove_2smpb_02e

sensor = grove_2smpb_02e.Grove2smpd02e()
app = Flask(__name__)


@app.route('/sensor')
def cpu():
    press, temp = sensor.readData()
    return jsonify(temperature=1, pressure=1)
   #  return jsonify(temperature=round(temp,2), pressure=round(press,2))

@app.route('/')
def home():
   return render_template('index.html') 


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)


