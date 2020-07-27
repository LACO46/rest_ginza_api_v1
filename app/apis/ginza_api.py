# -*- coding:utf-8 -*-
from dataclasses import dataclass
import spacy


@dataclass
class GinzaApiBaseResultModel:
    result: list


@dataclass
class GinzaApiSimilarityResultModel:
    result: float


class ginza_api_base:
    def ginza_result(self, word: str) -> GinzaApiBaseResultModel:
        nlp = spacy.load('ja_ginza')
        doc = nlp(word)

        return {
            'result': doc.sents
        }

    def ginza_vector(self, word: str) -> GinzaApiBaseResultModel:
        nlp = spacy.load('ja_ginza')
        doc = nlp(word)

        return {
            'result': doc
        }

    def ginza_cos(self, word1: str, word2: str) -> GinzaApiSimilarityResultModel:
        nlp = spacy.load('ja_ginza')
        nlp_word1 = nlp(word1)
        nlp_word2 = nlp(word2)

        return {
            'result': nlp_word1.similarity(nlp_word2)
        }
