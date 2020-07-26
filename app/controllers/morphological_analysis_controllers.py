# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug import local

# impor file
from logics import morphological_analysis_logics


class morphological_analysis_controller():
    def morphological_analysis(self, request: local.LocalProxy):
        # 変数を定義
        json = request.json
        morphological_analysis_logic = morphological_analysis_logics.morphological_analysis_logic()

        # jsonファイルが正常であることを確認
        if(not (json.keys() == {'word'})):
            return jsonify({'message': 'request json is injustice'}), 500

        return morphological_analysis_logic.morphological_analysis_base(json['word'])
