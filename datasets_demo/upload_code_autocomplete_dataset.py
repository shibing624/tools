# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""

"""Code AutoComplete Python dataset Corpus.(code_autocomplete)"""

import os

import datasets

_DESCRIPTION = """纯文本数据，内容：高质量编程源代码，包括Python，Java源代码"""

ATEC_HOME = "https://github.com/IceFlameWorm/NLP_Datasets/tree/master/ATEC"
BQ_HOME = "http://icrc.hitsz.edu.cn/info/1037/1162.htm"
LCQMC_HOME = "http://icrc.hitsz.edu.cn/Article/show/171.html"
PAWSX_HOME = "https://arxiv.org/abs/1908.11828"
STSB_HOME = "https://github.com/pluto-junzeng/CNSD"

_CITATION = "https://github.com/shibing624/code-autocomplete"

_DATA_URL = "https://github.com/shibing624/text2vec/releases/download/1.1.2/senteval_cn.zip"


class NliZhConfig(datasets.BuilderConfig):
    """BuilderConfig for NLI_zh"""

    def __init__(self, features, data_url, citation, url, label_classes=(0, 1), **kwargs):
        """BuilderConfig for NLI_zh
        Args:
          features: `list[string]`, list of the features that will appear in the
            feature dict. Should not include "label".
          data_url: `string`, url to download the zip file from.
          citation: `string`, citation for the data set.
          url: `string`, url for information about the data set.
          label_classes: `list[int]`, sim is 1, else 0.
          **kwargs: keyword arguments forwarded to super.
        """
        super().__init__(version=datasets.Version("1.0.0"), **kwargs)
        self.features = features
        self.label_classes = label_classes
        self.data_url = data_url
        self.citation = citation
        self.url = url


class NliZh(datasets.GeneratorBasedBuilder):
    """The Natural Language Inference Chinese(NLI_zh) Corpus."""

    BUILDER_CONFIGS = [
        NliZhConfig(
            name="ATEC",
            description=_DESCRIPTION,
            features=["sentence1", "sentence1"],
            data_url=_DATA_URL,
            citation=_CITATION,
            url=ATEC_HOME,
        ),
        NliZhConfig(
            name="BQ",
            description=_DESCRIPTION,
            features=["sentence1", "sentence1"],
            data_url=_DATA_URL,
            citation=_CITATION,
            url=BQ_HOME,
        ),
        NliZhConfig(
            name="LCQMC",
            description=_DESCRIPTION,
            features=["sentence1", "sentence1"],
            data_url=_DATA_URL,
            citation=_CITATION,
            url=LCQMC_HOME,
        ),
        NliZhConfig(
            name="PAWSX",
            description=_DESCRIPTION,
            features=["sentence1", "sentence1"],
            data_url=_DATA_URL,
            citation=_CITATION,
            url=PAWSX_HOME,
        ),
        NliZhConfig(
            name="STS-B",
            description=_DESCRIPTION,
            features=["sentence1", "sentence1"],
            data_url=_DATA_URL,
            citation=_CITATION,
            url=STSB_HOME,
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=self.config.description,
            features=datasets.Features(
                {
                    "sentence1": datasets.Value("string"),
                    "sentence2": datasets.Value("string"),
                    "label": datasets.Value("int32"),
                    # "idx": datasets.Value("int32"),
                }
            ),
            homepage=self.config.url,
            citation=self.config.citation,
        )

    def _split_generators(self, dl_manager):
        dl_dir = dl_manager.download_and_extract(self.config.data_url) or ""
        dl_dir = os.path.join(dl_dir, f"senteval_cn/{self.config.name}")
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": os.path.join(dl_dir, f"{self.config.name}.train.data"),
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "filepath": os.path.join(dl_dir, f"{self.config.name}.valid.data"),
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "filepath": os.path.join(dl_dir, f"{self.config.name}.test.data"),
                },
            ),
        ]

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) form."""
        with open(filepath, 'r', encoding="utf-8") as f:
            for idx, row in enumerate(f):
                # print(row)
                terms = row.split('\t')
                yield idx, {
                    "sentence1": terms[0],
                    "sentence2": terms[1],
                    "label": int(terms[2]),
                }
