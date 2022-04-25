# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from sentence_transformers import SentenceTransformer, util
from PIL import Image


def use_clip_official_demo():
    import torch
    import clip
    from PIL import Image

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)

    image = preprocess(Image.open("CLIP.png")).unsqueeze(0).to(device)
    text = clip.tokenize(["a diagram", "a dog", "a cat"]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]


def use_st_clip_demo():
    # Load CLIP model
    model = SentenceTransformer('clip-ViT-B-32')

    img = Image.open('./two_dogs_in_show.jpg')
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Encode an image:
    img_emb = model.encode(img)
    print(img_emb.shape)

    # Encode text descriptions
    text_emb = model.encode(['Two dogs in the snow', 'A cat on a table', 'A picture of London at night'])

    # Compute cosine similarities
    cos_scores = util.cos_sim(img_emb, text_emb)
    print(cos_scores)


def transformers_clip_demo():
    from PIL import Image
    from transformers import CLIPProcessor, CLIPModel

    model = CLIPModel.from_pretrained("/path/to/clip/model")
    processor = CLIPProcessor.from_pretrained("/path/to/clip/model")

    image = Image.open("./image.png")
    inputs = processor(images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)

    print(outputs)


def use_text2vec_model():
    from sentence_transformers import SentenceTransformer

    m = SentenceTransformer("shibing624/text2vec-base-chinese")
    sentences = ['如何更换花呗绑定银行卡', '花呗更改绑定银行卡']

    sentence_embeddings = m.encode(sentences)
    print("Sentence embeddings:")
    print(sentence_embeddings)


if __name__ == '__main__':
    use_text2vec_model()
