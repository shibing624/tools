# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:

blog refer: https://blog.ml6.eu/ocr-correction-with-byt5-5994d1217c07
"""
from dataclasses import dataclass, field
from typing import Optional
import os
from transformers import AutoTokenizer, T5ForConditionalGeneration
from transformers import HfArgumentParser, TrainingArguments, Trainer, set_seed
from datasets import load_dataset

import nlpaug.augmenter.char as nac


@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.

    Using `HfArgumentParser` we can turn this class
    into argparse arguments to be able to specify them on
    the command line.
    """

    max_len: Optional[int] = field(
        default=128,
        metadata={
            "help": "The maximum total input sequence length after tokenization. Sequences longer "
                    "than this will be truncated, sequences shorter will be padded."
        },
    )
    overwrite_cache: bool = field(
        default=False, metadata={"help": "Overwrite the cached preprocessed datasets or not."}
    )
    pad_to_max_length: bool = field(
        default=True,
        metadata={
            "help": "Whether to pad all samples to `max_seq_length`. "
                    "If False, will pad the samples dynamically when batching to the maximum length in the batch."
        },
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of training examples to this "
                    "value if set."
        },
    )
    max_eval_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of evaluation examples to this "
                    "value if set."
        },
    )
    max_predict_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of prediction examples to this "
                    "value if set."
        },
    )
    server_ip: Optional[str] = field(default=None, metadata={"help": "For distant debugging."})
    server_port: Optional[str] = field(default=None, metadata={"help": "For distant debugging."})


@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """

    model_name_or_path: str = field(
        default=None, metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )
    language: str = field(
        default=None, metadata={"help": "Evaluation language. Also train language if `train_language` is set to None."}
    )
    train_language: Optional[str] = field(
        default=None, metadata={"help": "Train language if it is different from the evaluation language."}
    )
    config_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained config name or path if not the same as model_name"}
    )
    tokenizer_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained tokenizer name or path if not the same as model_name"}
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={"help": "Where do you want to store the pretrained models downloaded from huggingface.co"},
    )
    do_lower_case: Optional[bool] = field(
        default=False,
        metadata={"help": "arg to indicate if tokenizer should do lower case in AutoTokenizer.from_pretrained()"},
    )
    use_fast_tokenizer: bool = field(
        default=True,
        metadata={"help": "Whether to use one of the fast tokenizer (backed by the tokenizers library) or not."},
    )
    model_revision: str = field(
        default="main",
        metadata={"help": "The specific model version to use (can be a branch name, tag name or commit id)."},
    )
    use_auth_token: bool = field(
        default=False,
        metadata={
            "help": "Will use the token generated when running `transformers-cli login` (necessary to use this script "
                    "with private models)."
        },
    )


def predict():
    example_sentence = "Ben algoritme dat op ba8i8 van kunstmatige inte11i9entie vkijwel geautomatiseerd een tekst herstelt met OCR fuuten."

    tokenizer = AutoTokenizer.from_pretrained('ml6team/byt5-base-dutch-ocr-correction')

    model_inputs = tokenizer(example_sentence, max_length=128, truncation=True, return_tensors="pt")

    model = T5ForConditionalGeneration.from_pretrained('ml6team/byt5-base-dutch-ocr-correction')
    outputs = model.generate(**model_inputs, max_length=128)

    tokenizer.decode(outputs[0])


def train():
    args_dict = {
        "model_name_or_path": 'google/byt5-small',
        "max_len": 128,
        "output_dir": './byt5-base-dutch-ocr-correction',
        "overwrite_output_dir": True,
        "per_device_train_batch_size": 2,
        "per_device_eval_batch_size": 2,
        "gradient_accumulation_steps": 4,
        "learning_rate": 5e-4,
        "warmup_steps": 250,
        "logging_steps": 100,
        "evaluation_strategy": "steps",
        "eval_steps": 250,
        "num_train_epochs": 4,
        "do_train": True,
        "do_eval": True,
        "fp16": False,
        "use_cache": False,
        "max_steps": 5000
    }
    parser = HfArgumentParser(
        (ModelArguments, DataTrainingArguments, TrainingArguments))
    model_args, data_args, training_args = parser.parse_dict(args_dict)
    set_seed(training_args.seed)
    dataset = load_dataset('csv', data_files={'train': ['data/nl_test_20.csv'], 'test': 'data/nl_test_20.csv'})

    # dataset: oscar, unshuffled_deduplicated_en train
    # dataset = load_dataset('oscar', 'unshuffled_deduplicated_en', language='en')
    # print(dataset)

    # dataset = load_dataset('csv', data_files={'train': ['data/nl_unshuffled_test_10_000.csv'],
    #                                           'test': 'data/nl_unshuffled_test_10_000.csv'})
    print(dataset)

    # Load pretrained model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_args.tokenizer_name if model_args.tokenizer_name else model_args.model_name_or_path,
        cache_dir=model_args.cache_dir,
        max_length=data_args.max_len
    )
    model = T5ForConditionalGeneration.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=model_args.cache_dir,
    )

    # overwriting the default max_length of 20
    tokenizer.model_max_length = 128
    model.config.max_length = 128

    def chunk_text(text, tokenizer, max_seq_length):
        tokens = tokenizer.encode(text, max_length=max_seq_length, truncation=True)
        return tokens

    dataset = dataset.map(
        lambda x: chunk_text(x['text'],
                             tokenizer,
                             128),
        batched=True,
        remove_columns=["text"])

    def ocr_augment_chars(text, **kwargs):
        aug = nac.OcrAug(**kwargs)

        augmented_data = aug.augment(text)
        return augmented_data

    # Augmenting the dataset with common OCR errors
    dataset = dataset.map(
        lambda x: {'ocr_text': ocr_augment_chars(x['text'], aug_char_p=0.4, aug_word_p=0.6), 'text': x['text']},
        batched=True, remove_columns=["text"])

    train_dataset = dataset['train']
    valid_dataset = dataset['test']

    train_dataset = train_dataset.select(range(100000))
    valid_dataset = valid_dataset.select(range(10000))

    def prep_dataset(tokenizer, dataset, max_len):
        def convert_to_features(example_batch):
            input_encodings = tokenizer.batch_encode_plus(example_batch['ocr_text'],
                                                          truncation=True,
                                                          padding='max_length',
                                                          max_length=max_len,
                                                          example_batch=2,
                                                          )
            target_encodings = tokenizer.batch_encode_plus(example_batch['text'],
                                                           truncation=True,
                                                           padding='max_length',
                                                           max_length=max_len)

            encodings = {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'target_ids': target_encodings['input_ids'],
                'target_attention_mask': target_encodings['attention_mask']
            }

            return encodings

        dataset = dataset.map(convert_to_features, batched=True)
        # Set the tensor type and the columns which the dataset should return
        columns = ['input_ids', 'target_ids',
                   'attention_mask', 'target_attention_mask']
        dataset.with_format(type='torch', columns=columns)
        # Rename columns to the names that the forward method of the selected
        # model expects
        dataset = dataset.rename_column('target_ids', 'labels')
        dataset = dataset.rename_column('target_attention_mask', 'decoder_attention_mask')
        dataset = dataset.remove_columns(['text', 'ocr_text'])
        return dataset

    train_dataset = prep_dataset(tokenizer, train_dataset, data_args.max_len)
    valid_dataset = prep_dataset(tokenizer, valid_dataset, data_args.max_len)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
    )

    trainer.train(
        model_path=model_args.model_name_or_path if os.path.isdir(
            model_args.model_name_or_path) else None
    )

    trainer.save_model()
    # For convenience, we also re-save the tokenizer to the same directory,
    # so that you can share your model easily on huggingface.co/models =)
    tokenizer.save_pretrained(training_args.output_dir)


if __name__ == '__main__':
    train()
