# -*- coding:utf-8 -*-
from dataclasses import dataclass
from apis import test_api

# レスポンスの型
@dataclass
class GinzaResultModel:
    statu_code: int
    word: str
    result: [test_api.GinzaApiResultModel]


# テスト用のクラス
class test:
    # ginza apiのテストを行う関数
    def ginza_test(self):
        # 変数
        test = test_api.test()
        word = '銀座でランチをご一緒しましょう。'

        # resultからレスポンスの作成
        result: test_api.GinzaResultModel = {
            'statu_code': 200,
            'word': word,
            'result': test.ginza_test(word)      # apiの呼び出し
        }

        return result
