# -*- coding:utf-8 -*-
from dataclasses import dataclass

# import file
from apis import ginza_api


# resultの型
@dataclass
class GinzaApiResultModel:
    count: int        # トークン番号
    text: str         # テキスト
    reading: str      # 読みカナ
    lemma: str        # 基本形
    pos: str          # 品詞
    tag: [str]        # 品詞詳細
    dep: str          # トークンと各トークンの依存関係
    head: int         # 依存関係の親のトークン
    inf: str          # 活用情報


# レスポンスの型
@dataclass
class GinzaResultResponseModel:
    statu_code: int
    word: str
    result: [GinzaApiResultModel]


# ginzaを利用した形態素解析を行うクラス
class morphological_analysis_logic:
    # 形態素解析の結果を返す関数
    def morphological_analysis_base(self, word: str):
        # 変数
        ginza_api_base = ginza_api.ginza_api_base()

        # apiの呼び出し
        ginza_result: ginza_api.GinzaApiBaseResultModel = ginza_api_base.ginza_result(
            word)

        ginza_api_result = []
        # ginza apiの結果から形態素解析の結果を取得
        for sent in ginza_result['result']:
            for token in sent:
                # ginza apiの結果をresultの型に合わせる
                result: GinzaApiResultModel = {
                    'count': token.i,
                    'text': token.text,
                    'reading': token._.reading,
                    'lemma': token.lemma_,
                    'pos': token.pos_,
                    'tag': token.tag_.split("-"),
                    'dep': token.dep_,
                    'head': token.head.i,
                    'inf': token._.inf
                }
                ginza_api_result.append(result)

        # resultからレスポンスの作成
        ginza_result_response: GinzaResultResponseModel = {
            'statu_code': 200,
            'word': word,
            'result': ginza_api_result
        }

        return ginza_result_response
