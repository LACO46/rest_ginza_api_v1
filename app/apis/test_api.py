# -*- coding:utf-8 -*-
from dataclasses import dataclass
import spacy


@dataclass
class GinzaApiResultModel:
    count: int
    orth: str
    lemma: str
    pos: str
    tag: str
    dep: str
    head: str


class test:
    def ginza_test(self, word: str) -> [GinzaApiResultModel]:
        nlp = spacy.load('ja_ginza')
        doc = nlp(word)

        ginza_result = []

        for sent in doc.sents:
            for token in sent:
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
