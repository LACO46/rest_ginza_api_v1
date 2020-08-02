# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


# resultの型
@dataclass
class GinzaApiResultModel:
    text: str
    vector: [float]


# レスポンスの型
@dataclass
class GinzaResultResponseModel:
    statu_code: int
    word: str
    result: [GinzaApiResultModel]


# 文字を数値で返すクラス
class word_number_array_logic:
    # 文字の１００次元配列を取得する関数
    def word_number_array(self, word: str):
        # 変数
        ginza_api_base = ginza_api.ginza_api_base()

        # apiの呼び出し
        ginza_result = ginza_api_base.ginza_vector(word)

        # 単語ごとに文字の１００次元配列を取得する
        ginza_api_result = []
        for token in ginza_result['result']:
            result: GinzaApiResultModel = {
                'text': str(token),
                'vector': list(map(float, list(token.vector)))
            }
            ginza_api_result.append(result)

        # resultからレスポンスの作成
        ginza_result_response: GinzaResultResponseModel = {
            'statu_code': 200,
            'word': word,
            'result': ginza_api_result
        }
        return ginza_result_response
