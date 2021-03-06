# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request

# import file
from controllers import (
    test_controller,
    morphological_analysis_controllers,
    word_number_array_controllers,
    word_cos_controllers,
    update_dict_controllers,
    add_dict_controllers)


class urls:
    app = Flask(__name__)
    # jsonをascii codeで取得
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        # 変数
        test = test_controller.test()

        # レスポンスを返す
        return test.ginza_test()

    @app.route('/v1/morphological-analysis/', methods=['POST'])
    def morphological_analysis():
        # 変数
        morphological_analysis_controller = morphological_analysis_controllers.morphological_analysis_controller()

        # レスポンスを返す
        return morphological_analysis_controller.morphological_analysis(request)

    @app.route('/v1/word-number-array/', methods=['POST'])
    def word_number_array():
        # 変数
        word_number_array_controller = word_number_array_controllers.word_number_array_controller()

        # レスポンスを返す
        return word_number_array_controller.word_number_array(request)

    @app.route('/v1/word-cos/', methods=['POST'])
    def word_cos():
        # 変数
        word_cos_controller = word_cos_controllers.word_cos_controller()

        # レスポンスを返す
        return word_cos_controller.word_cos(request)

    @app.route('/v1/add-dict/', methods=['POST'])
    def add_dict():
        # 変数
        add_dict_controller = add_dict_controllers.add_dict_controller()

        # レスポンスを返す
        return add_dict_controller.add_dict(request)

    @app.route('/v1/update-dict/', methods=['GET'])
    def update_dict():
        # 変数
        update_dict_controller = update_dict_controllers.update_dict_controller()

        # レスポンスを返す
        return update_dict_controller.update_dict()
