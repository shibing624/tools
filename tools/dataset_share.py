# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from datasets import DatasetInfo, Features, Split, SplitGenerator, GeneratorBasedBuilder, Value, Sequence
import json


class MyDataset(GeneratorBasedBuilder):
    def _info(self):
        return DatasetInfo(
            features=Features({
                "questions": Sequence(Value("string")),
                "answers": Sequence(Value("string"))
            }),
            supervised_keys=("questions", "answers"),
            homepage="https://github.com/FreedomIntelligence/Huatuo-26M",
            citation='''
            @misc{li2023huatuo26m,
                  title={Huatuo-26M, a Large-scale Chinese Medical QA Dataset}, 
                  author={Jianquan Li and Xidong Wang and Xiangbo Wu and Zhiyi Zhang and Xiaolong Xu and Jie Fu and Prayag Tiwari and Xiang Wan and Benyou Wang},
                  year={2023},
                  eprint={2305.01526},
                  archivePrefix={arXiv},
                  primaryClass={cs.CL}
            }

            ''',
        )

    def _split_generators(self, dl_manager):
        train_path = "train_datasets.jsonl"
        validation_path = "validation_datasets.jsonl"
        test_path = "test_datasets.jsonl"

        return [
            SplitGenerator(name=Split.TRAIN, gen_kwargs={"filepath": train_path}),
            SplitGenerator(name=Split.VALIDATION, gen_kwargs={"filepath": validation_path}),
            SplitGenerator(name=Split.TEST, gen_kwargs={"filepath": test_path}),
        ]

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            for id_, row in enumerate(f):
                # Process your data here and create a dictionary with the features.
                # For example, if your data is in JSON format:
                data = json.loads(row)
                yield id_, {
                    "questions": data["questions"],
                    "answers": data["answers"],
                }


if __name__ == '__main__':
    from datasets import load_dataset

    dataset = load_dataset("shibing624/medical", 'finetune', num_proc=10)

    print(dataset)
    print(dataset['train'].shuffle()[:10])
    print(dataset['train'][-10:])