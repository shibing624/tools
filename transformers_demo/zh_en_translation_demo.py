# -*- coding: utf-8 -*-
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
inputs = tokenizer(
    ">>cmn<< Facebook is a technology company based in New York and Paris",
    return_tensors="pt"
)
outputs = model.generate(inputs["input_ids"], max_length=40, num_beams=4, early_stopping=True)

print(tokenizer.decode(outputs[0]))

s = [
    "The boar that was running forward, got cut from the sharp net and his head split into two. The younger brother tied the boar onto his shoulders and headed for the castle.",
    "Big brother! Let's go to the castle and share this happiness. The little brother, being so tired, fell asleep after drinking the wine.",
    "This repository contains the source code and trained model for Joint Retrieval and Generation Training for Grounded Text Generation. RetGen is a joint training framework that simultaneously optimizes a dense passage retriever and a knowledge-grounded text generator in an end-to-end fashion. It can be applied to scenarios including but not limited to conversational modeling, text generation and open-domain question answering. The code implementation is based on DialoGPT, Huggingface Transformers, DPR and ANCE. Our human evaluation results indicates that RetGen can generate more relevant, interesting and human-like text comparing to vanilla DialoGPT or GPT-2.",
]
for i in s:
    inputs = tokenizer(f">>cmn<< {i}", return_tensors="pt")
    print(i, inputs["input_ids"])
    outputs = model.generate(inputs["input_ids"], max_length=128, num_beams=4, early_stopping=True)
    print(tokenizer.decode(outputs[0]))

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
inputs = tokenizer(
    "我爱中国，我住在北京朝阳区。南京市长江大桥回到家里，家里是住在长江大桥的边上。",
    return_tensors="pt"
)
outputs = model.generate(inputs["input_ids"], max_length=40, num_beams=4, early_stopping=True)

print(tokenizer.decode(outputs[0]))
