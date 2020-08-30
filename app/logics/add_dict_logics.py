# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import text_api, compilation_dict

# requestの型
@dataclass
class RequestModel:
    headline: str
    left_connection_id: str
    right_connection_id: str
    cost: str
    part_of_speech_one: str
    part_of_speech_two: str
    part_of_speech_three: str
    part_of_speech_four: str
    part_of_speech_advanced_type: str
    part_of_speech_inflected_form: str
    reading: str
    normalized_notation: str
    dictionary_id: str
    split_type: str
    a_unit_division_information: str
    b_unit_division_information: str
    unused: str


class add_dict_logic:
    # 形態素解析の辞書の更新をするロジック
    def add_dict(self, req: RequestModel) -> bool:
        text = text_api.text()
        compilation_dict_base = compilation_dict.compilation_dict_base()

        add_content = "\n{0},{1},{2},{3},{0},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16}".format(
            req['headline'],
            req['left_connection_id'],
            req['right_connection_id'],
            req['cost'],
            req['part_of_speech_one'],
            req['part_of_speech_two'],
            req['part_of_speech_three'],
            req['part_of_speech_four'],
            req['part_of_speech_advanced_type'],
            req['part_of_speech_inflected_form'],
            req['reading'],
            req['normalized_notation'],
            req['dictionary_id'],
            req['split_type'],
            req['a_unit_division_information'],
            req['b_unit_division_information'],
            req['unused'])

        is_content_add_success = text.add_content_api(
            file_path='user_dict/user_dict.csv', content=add_content)
        if not (is_content_add_success):
            return False

        is_compilation_success = compilation_dict_base.compilation_dict()
        if not (is_compilation_success):
            return False

        return True
