# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug import local

# impor file
from logics import word_cos_logics


class word_cos_controller():
    def word_cos(self, request: local.LocalProxy):
        json = request.json
        # 変数を定義
        word_cos_logic = word_cos_logics.word_cos_logic()

        # jsonファイルが正常であることを確認
        if (not (json.keys() == {'word1', 'word2'})):
            return jsonify({'message': 'request json is injustice'}), 500

        return word_cos_logic.word_cos(word1=json['word1'], word2=json['word2'])
