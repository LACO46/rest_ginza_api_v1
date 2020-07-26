# -*- coding:utf-8 -*-
from dataclasses import dataclass
import spacy


@dataclass
class GinzaApiBaseResultModel:
    result: list


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
