# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug import local

# impor file
from logics import word_number_array_logics


class word_number_array_controller():
    def word_number_array(self, request: local.LocalProxy):
        # 変数を定義
        json = request.json
        word_number_array_logic = word_number_array_logics.word_number_array_logic()

        # jsonファイルが正常であることを確認
        if(not (json.keys() == {'word'})):
            return jsonify({'message': 'request json is injustice'}), 500

        return word_number_array_logic.word_number_array(json['word'])
