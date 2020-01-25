# -*- coding: utf-8 -*-
import requests
from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import CORS

from werkzeug.exceptions import HTTPException

import os
import logging
import logging.config

# utils
from utils import sum_digits

# setup log file
_PATH = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.join(_PATH, 'configs/logging.ini')
DEFAULT_LOG_CONFIG = os.path.abspath(_PATH)

logging.config.fileConfig(DEFAULT_LOG_CONFIG)
# log controller
logger2 = logging.getLogger('flask')

# setup flask service
app = Flask(__name__)
CORS(app)

@app.route('/helloworld')
def helloworld():
    return 'helloworld', 200

@app.route('/api/parse/sumDigit', methods=['POST'])
def handle_sum_digits():
    handler = sum_digits.SumDigits(request.json['content'])
    return str(handler.get_sum()), 200

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    logger2.error('%s', str(e))
    return jsonify(error=str(e)), code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

