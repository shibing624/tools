# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import logging
from abc import ABC, abstractmethod
from typing import Iterable, List

import requests
import numpy as np

logger = logging.getLogger(__name__)


class Encoder(ABC):
    """A shared encoder interface.
    Each client must provide an encode() method and a FEATURE_SIZE
    constant indicating the size of encoded vectors"""

    FEATURE_SIZE: int

    @abstractmethod
    def encode(self, data: Iterable[str]) -> np.array:
        pass


class UniversalEncoderError(Exception):
    pass


class UniversalEncoder(Encoder):
    """
        Requests-based client for the Universal Sentence Encoder TF model
    """

    # Length of returned vectors
    FEATURE_SIZE = 512
    BATCH_SIZE = 32

    def __init__(self, host, port):
        self.server_url = "http://{host}:{port}".format(
            host=host,
            port=port,
        )

    @staticmethod
    def _sanitize_input(sentence: str):
        return sentence.replace('\n', '').lower().strip()[:1000]

    def encode(self, data: Iterable[str]) -> np.array:
        logger.debug(f"Encode request: {data}")
        data = [self._sanitize_input(sentence) for sentence in data]
        all_vectors: List[List[float]] = []

        for i in range(0, len(data), self.BATCH_SIZE):
            batch = data[i:i + self.BATCH_SIZE]
            response = requests.post(
                url=self.server_url,
                json={
                    "model_name": "default",
                    "model_version": "00000001",
                    "data": {
                        "text": batch
                    }
                }
            )
            if not response.ok:
                raise UniversalEncoderError(
                    f"Bad response from encoder: {response}"
                )
            all_vectors += response.json()['embeddings']

        return np.array(all_vectors).astype(np.float32)
