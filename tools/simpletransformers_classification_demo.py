# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import pandas as pd
import torch

from simpletransformers.classification import ClassificationModel

# Train and Evaluation data needs to be in a Pandas Dataframe containing at least two columns. If the Dataframe has a header, it should contain a 'text' and a 'labels' column. If no header is present, the Dataframe should contain at least two columns, with the first column is the text with type str, and the second column in the label with type int.
train_data = [
    ["Example sentence belonging to class 1", 1],
    ["Example sentence belonging to class 0", 0],
    ["Example eval senntence belonging to class 2", 2],
]
train_df = pd.DataFrame(train_data)

eval_data = [
    ["Example eval sentence belonging to class 1", 1],
    ["Example eval sentence belonging to class 0", 0],
    ["Example eval senntence belonging to class 2", 2],
]
eval_df = pd.DataFrame(eval_data)

# Create a ClassificationModel
model = ClassificationModel(
    "bert",
    "outputs",
    use_cuda=False,
    num_labels=3,
    args={"reprocess_input_data": True, "overwrite_output_dir": True,
          'num_train_epochs':1},
)
if __name__ == '__main__':
    # Train the model
    # model.train_model(train_df)
    # model_path = 'outputs/'
    # torch.load("outputs/pytorch_model.bin")
    # model.from_pretrained('outputs/')
    # Evaluate the model
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)
    print('eval: ', result, model_outputs, wrong_predictions)
    predictions, raw_outputs = model.predict(["Some arbitary sentence"])
    print('pred: ', predictions, raw_outputs)
    predict_proba = 0.
    for raw_output, prediction in zip(raw_outputs, predictions):
        predict_proba = raw_output[prediction]
    print(predict_proba)
