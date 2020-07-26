# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


@dataclass
class GinzaApiResultModel:
    text: str
    vector: [float]


@dataclass
class GinzaResultResponseModel:
    statu_code: int
    word: str
    result: [GinzaApiResultModel]


class word_number_array_logic:
    def word_number_array(self, word: str):
        ginza_api_base = ginza_api.ginza_api_base()
        ginza_result = ginza_api_base.ginza_vector(word)

        ginza_api_result = []
        for token in ginza_result['result']:
            result: GinzaApiResultModel = {
                'text': str(token),
                'vector': list(map(float, list(token.vector)))
            }
            ginza_api_result.append(result)

        ginza_result_response: GinzaResultResponseModel = {
            'statu_code': 200,
            'word': word,
            'result': ginza_api_result
        }
        return ginza_result_response
