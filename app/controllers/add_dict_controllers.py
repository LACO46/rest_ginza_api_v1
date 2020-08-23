# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug import local

# import file


class add_dict_controller:
    # 形態素解析の辞書の更新をするコントローラ
    def add_dict(self, request: local.LocalProxy):
        # 変数を定義
        json = request.json
        key_check_result = json.keys() >= {'headline', 'left_connection_id',
                                           'right_connection_id', 'cost',
                                           'headline', 'part_of_speech_one',
                                           'part_of_speech_two',
                                           'part_of_speech_three',
                                           'part_of_speech_four',
                                           'part_of_speech_advanced_type',
                                           'part_of_speech_inflected_form',
                                           'reading', 'normalized_notation',
                                           'dictionary_id', 'split_type',
                                           'a_unit_division_information',
                                           'b_unit_division_information', 'unused'}

        if not (key_check_result):
            return jsonify({'message': 'request json is injustice'}), 500

        return "hello world"
