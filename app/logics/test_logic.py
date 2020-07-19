# -*- coding:utf-8 -*-
from dataclasses import dataclass
from apis import test_api


@dataclass
class GinzaResultModel:
    statu_code: int
    word: str
    result: [test_api.GinzaApiResultModel]


class test:
    def ginza_test(self):
        test = test_api.test()
        word = '銀座でランチをご一緒しましょう。'

        result: test_api.GinzaResultModel = {
            'statu_code': 200,
            'word': word,
            'result': test.ginza_test(word)
        }

        return result
