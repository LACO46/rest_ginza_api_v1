# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request

# import file
from controllers import (test_controller)


class urls:
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        test = test_controller.test()
        return test.ginza_test()
