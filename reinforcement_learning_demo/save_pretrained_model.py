
import torch
from transformers import pipeline, AutoTokenizer, AutoModel
device = 0 if torch.cuda.is_available() else "cpu" 
sentiment_pipe = pipeline("sentiment-analysis", model="lvwerra/distilbert-imdb", device=device)

"""The model outputs are the logits for the negative and positive class. We will use the logits for positive class as a reward signal for the language model."""

text = 'this movie was really bad!!'
r = sentiment_pipe(text)
print(text, r)

save_directory = '/apdcephfs/private_flemingxu/models/lvwerra-distilbert-imdb'
sentiment_pipe.model.save_pretrained(save_directory)
sentiment_pipe.tokenizer.save_pretrained(save_directory)