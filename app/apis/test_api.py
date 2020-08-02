# -*- coding:utf-8 -*-
from dataclasses import dataclass
import spacy


# ginzaのテストのレスポンスの型
@dataclass
class GinzaApiResultModel:
    count: int
    orth: str
    lemma: str
    pos: str
    tag: str
    dep: str
    head: str


# ginzaのテストのクラス
class test:
    # ginzaのテストを行う関数
    def ginza_test(self, word: str) -> [GinzaApiResultModel]:
        # ginzaの形態素解析の結果を返す関数
        nlp = spacy.load('ja_ginza')

        # wordをginzaに読み込ませる
        doc = nlp(word)

        ginza_result = []

        # ginzaの形態素解析の結果を取得
        for sent in doc.sents:
            for token in sent:
                # ginzaのテストのレスポンスの型に合わせて形態素解析の結果を格納
                result: GinzaApiResultModel = {
                    'count': token.i,
                    'orth': token.orth_,
                    'lemma': token.lemma_,
                    'pos': token.pos_,
                    'tag': token.tag_,
                    'dep': token.dep_,
                    'head': token.head.i
                }
                ginza_result.append(result)

        return ginza_result
