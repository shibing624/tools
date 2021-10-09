# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import faiss
from encoder import UniversalEncoder
import numpy as np
# Don't forget to start the encoder container locally and open the 8501 port
from sentence_transformers import SentenceTransformer
encoder = UniversalEncoder(host='localhost', port=8501)
data = [
    'What color is chameleon?',
    'When is the festival of colors?',
    'When is the next music festival?',
    'How far is the moon?',
    'How far is the sun?',
    'What happens when the sun goes down?',
    'What we do in the shadows?',
    'What is the meaning of all this?',
    'What is the meaning of Russel\'s paradox?',
    'How are you doing?'
]
encoded_data = encoder.encode(data)

# We're going to use a regular "Flat Inner Product" index here
# as we're not storing millions of rows.
# We'll also wrap it in the IndexIDMap just to demonstrate
# how you can store actual document IDs right in the index
# and get them back along with the found vectors when searching

index = faiss.IndexIDMap(faiss.IndexFlatIP(encoder.FEATURE_SIZE))
index.add_with_ids(encoded_data, np.array(range(0, len(data))))


def search(query):
    query_vector = encoder.encode([query])
    k = 1
    top_k = index.search(query_vector, k)
    return [
        data[_id] for _id in top_k[1].tolist()[0]
    ]


# Examples:

print(search("When is Holi?"))

# >>> ['When is the festival of colors?']
