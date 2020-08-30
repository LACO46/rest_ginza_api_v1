# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
from werkzeug import local

# import file
from logics import add_dict_logics


class add_dict_controller:
    # 形態素解析の辞書の更新をするコントローラ
    def add_dict(self, request: local.LocalProxy):
        # 変数を定義
        json = request.json
        add_dict_logic = add_dict_logics.add_dict_logic()
        key_check_result = json.keys() >= {'headline', 'left_connection_id',
                                           'right_connection_id', 'cost',
                                           'part_of_speech_one',
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

        is_add_dict_success = add_dict_logic.add_dict(req=json)
        if not (is_add_dict_success):
            return "add dict faild"

        return "add dict success"
