# -*- coding:utf-8 -*-
from dataclasses import dataclass
import spacy


# ginzaの基本のレスポンスの型
@dataclass
class GinzaApiBaseResultModel:
    result: list


# ginzaのcosのレスポンスの型
@dataclass
class GinzaApiSimilarityResultModel:
    result: float


# ginza apiを定義するクラス
class ginza_api_base:
    # ginzaの形態素解析の結果を返す関数
    def ginza_result(self, word: str) -> GinzaApiBaseResultModel:
        # 形態素解析を行う言語を日本語に設定
        nlp = spacy.load('ja_ginza')

        # wordをginzaに読み込ませる
        doc = nlp(word)

        return {
            'result': doc.sents
        }

    # 単語を表す１００次元配列を取得
    def ginza_vector(self, word: str) -> GinzaApiBaseResultModel:
        # 単語を表す１００次元配列を取得する言語を日本語に設定
        nlp = spacy.load('ja_ginza')

        # wordをginzaに読み込ませる
        doc = nlp(word)

        # ginzaの基本のレスポンスの型に合わせて値を返す
        return {
            'result': doc
        }

    # 単語ごとの類似度のcosを取得
    def ginza_cos(self, word1: str, word2: str) -> GinzaApiSimilarityResultModel:
        # 単語ごとの類似度のcosを取得する言語を日本語に設定
        nlp = spacy.load('ja_ginza')

        # word1とword2をginzaに読み込ませる
        nlp_word1 = nlp(word1)
        nlp_word2 = nlp(word2)

        # ginzaのcosのレスポンスの型に合わせて値を返す
        return {
            'result': nlp_word1.similarity(nlp_word2)
        }
