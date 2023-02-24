# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import spacy
from spacy.lang.zh.examples import sentences
nlp = spacy.load("zh_core_web_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)


nlp = spacy.load("zh_core_web_sm")
total_doc=''.join(sentences)
nlp.add_pipe('sentencizer', name='sentence_segmenter', before='parser')
doc = nlp(total_doc)
print(doc.text)
for token in doc:
    print(token)
    print(token.is_sent_start)
for sent in doc.sents:
    print(sent)
