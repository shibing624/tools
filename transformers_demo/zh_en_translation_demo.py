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


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
inputs = tokenizer(
    "我爱中国，我住在北京朝阳区。南京市长江大桥回到家里，家里是住在长江大桥的边上。",
    return_tensors="pt"
)
outputs = model.generate(inputs["input_ids"], max_length=40, num_beams=4, early_stopping=True)

print(tokenizer.decode(outputs[0]))



