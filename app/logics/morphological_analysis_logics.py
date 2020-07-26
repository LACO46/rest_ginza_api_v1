# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


@dataclass
class GinzaApiResultModel:
    count: int
    orth: str
    lemma: str
    pos: str
    tag: [str]
    dep: str
    head: str


@dataclass
class GinzaResultResponseModel:
    statu_code: int
    word: str
    result: [GinzaApiResultModel]


class morphological_analysis_logic:
    def morphological_analysis_base(self, word: str):
        ginza_api_base = ginza_api.ginza_api_base()
        ginza_result: ginza_api.GinzaApiBaseResultModel = ginza_api_base.ginza_result(
            word)

        ginza_api_result = []
        for sent in ginza_result['result']:
            for token in sent:
                result: GinzaApiResultModel = {
                    'count': token.i,
                    'orth': token.orth_,
                    'lemma': token.lemma_,
                    'pos': token.pos_,
                    'tag': token.tag_.split("-"),
                    'dep': token.dep_,
                    'head': token.head.i
                }
                ginza_api_result.append(result)

        ginza_result_response: GinzaResultResponseModel = {
            'statu_code': 200,
            'word': word,
            'result': ginza_api_result
        }

        return ginza_result_response
