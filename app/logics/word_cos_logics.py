# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


@dataclass
class GinzaApiResultModel:
    statu_code: int
    word1: str
    word2: str
    result: float


class word_cos_logic:
    def word_cos(self, word1: str, word2: str):
        ginza_api_base = ginza_api.ginza_api_base()
        ginza_cos = ginza_api_base.ginza_cos
        ginza_cos_result = ginza_cos(word1=word1, word2=word2)

        result: GinzaApiResultModel = {
            'statu_code': 200,
            'word1': word1,
            'word2': word2,
            'result': ginza_cos_result['result']
        }

        return result
