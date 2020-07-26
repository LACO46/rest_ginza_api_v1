# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request

# import file
from controllers import (
    test_controller, morphological_analysis_controllers, word_number_array_controllers)


class urls:
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        test = test_controller.test()
        return test.ginza_test()

    @app.route('/v1/morphological-analysis/', methods=['POST'])
    def morphological_analysis():
        morphological_analysis_controller = morphological_analysis_controllers.morphological_analysis_controller()
        return morphological_analysis_controller.morphological_analysis(request)

    @app.route('/v1/word-number-array/', methods=['POST'])
    def word_number_array():
        word_number_array_controller = word_number_array_controllers.word_number_array_controller()
        return word_number_array_controller.word_number_array(request)
