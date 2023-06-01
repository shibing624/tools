from dataclasses import dataclass, field
from typing import Optional

import torch
from datasets import load_dataset

imdb = load_dataset("imdb")
imdb.save_to_disk('/apdcephfs/private_flemingxu/datasets/imdb')


dataset_name = 'BelleGroup/generated_train_0.5M_CN'
dataset = load_dataset(dataset_name)
print(dataset)
dataset = load_dataset(dataset_name, split="train")
print(dataset)
small_dataset = dataset.select([0, 10, 20, 30, 40, 50])
print(len(small_dataset))
print(small_dataset)

dataset = dataset.select(range(5000))
# Save in JSON Lines format
dataset.to_json(f"my-dataset.json")
dataset.to_csv('my-dataset.csv')
# Reload with the `json` script
json_datasets_reloaded = load_dataset("json", data_files='my-dataset.json')
print(json_datasets_reloaded)
print(next(iter(json_datasets_reloaded)))
