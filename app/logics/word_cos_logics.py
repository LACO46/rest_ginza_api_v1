# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


# resultの型
@dataclass
class GinzaApiResultModel:
    statu_code: int
    word1: str
    word2: str
    result: float


# 2つの文字の類似度で返すクラス
class word_cos_logic:
    # 2つの文字のcosを取得する関数
    def word_cos(self, word1: str, word2: str):
        # 変数
        ginza_api_base = ginza_api.ginza_api_base()

        # apiの呼び出し
        ginza_cos_result = ginza_api_base.ginza_cos(word1=word1, word2=word2)

        # resultからレスポンスの作成
        result: GinzaApiResultModel = {
            'statu_code': 200,
            'word1': word1,
            'word2': word2,
            'result': ginza_cos_result['result']
        }

        return result
