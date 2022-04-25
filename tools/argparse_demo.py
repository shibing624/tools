# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse
from enum import Enum


class EncoderType(Enum):
    FIRST_LAST_AVG = 0
    LAST_AVG = 1
    CLS = 2
    POOLER = 3
    MEAN = 4

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return EncoderType[s]
        except KeyError:
            raise ValueError()


def get_args():
    parser = argparse.ArgumentParser('Text Matching task')
    parser.add_argument('--model_arch', default='cosent', nargs='?',
                        choices=['cosent', 'sentencebert', 'bert'], help='model architecture')
    parser.add_argument('--task_name', default='STS-B', nargs='?',
                        choices=['ATEC', 'STS-B', 'BQ', 'LCQMC', 'PAWSX'], help='task name of dataset')
    parser.add_argument('--model_name', default='hfl/chinese-macbert-base', type=str,
                        help='Transformers model model or path')
    parser.add_argument("--do_train", action="store_true", help="Whether to run training.")
    parser.add_argument("--do_predict", action="store_true", help="Whether to run predict.")
    parser.add_argument('--output_dir', default='./outputs/STS-B-model', type=str, help='Model output directory')
    parser.add_argument('--max_seq_length', default=64, type=int, help='Max sequence length')
    parser.add_argument('--num_epochs', default=10, type=int, help='Number of training epochs')
    parser.add_argument('--batch_size', default=64, type=int, help='Batch size')
    parser.add_argument('--learning_rate', default=2e-5, type=float, help='Learning rate')
    parser.add_argument('--encoder_type', default='FIRST_LAST_AVG', type=lambda t: EncoderType[t],
                        choices=list(EncoderType), help='Encoder type, string name of EncoderType')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    get_args()
