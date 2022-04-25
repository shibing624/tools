# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import torch
from torch import nn
from transformers import BertModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize


class Model(nn.Module):
    def __init__(self, model_name='bert-base-chinese'):
        super(Model, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)

    def forward(self, input_ids, attention_mask, encoder_type='fist-last-avg'):
        """
        :param input_ids:
        :param attention_mask:
        :param encoder_type: encoder_type:  "first-last-avg", "last-avg", "cls", "pooler(cls + dense)"
        :return:
        """
        output = self.bert(input_ids, attention_mask, output_hidden_states=True)

        if encoder_type == 'fist-last-avg':
            # 第一层和最后一层的隐层取出  然后经过平均池化
            first = output.hidden_states[1]  # hidden_states列表有13个hidden_state，第一个其实是embeddings，第二个元素才是第一层的hidden_state
            last = output.hidden_states[-1]
            seq_length = first.size(1)  # 序列长度

            first_avg = torch.avg_pool1d(first.transpose(1, 2), kernel_size=seq_length).squeeze(-1)  # batch, hid_size
            last_avg = torch.avg_pool1d(last.transpose(1, 2), kernel_size=seq_length).squeeze(-1)  # batch, hid_size
            final_encoding = torch.avg_pool1d(
                torch.cat([first_avg.unsqueeze(1), last_avg.unsqueeze(1)], dim=1).transpose(1, 2),
                kernel_size=2).squeeze(-1)
            return final_encoding

        if encoder_type == 'last-avg':
            sequence_output = output.last_hidden_state  # (batch_size, max_len, hidden_size)
            seq_length = sequence_output.size(1)
            final_encoding = torch.avg_pool1d(sequence_output.transpose(1, 2), kernel_size=seq_length).squeeze(-1)
            return final_encoding

        if encoder_type == "cls":
            sequence_output = output.last_hidden_state
            cls = sequence_output[:, 0]  # [b,d]
            return cls

        if encoder_type == "pooler":
            pooler_output = output.pooler_output  # [b,d]
            return pooler_output

        if encoder_type == "dissecting":
            features = output[1]
            all_layer_embedding = torch.stack(features).permute(1, 0, 2, 3).cpu().numpy()

            unmask_num = np.sum(attention_mask, axis=1) - 1  # Not considering the last item
            all_layer_embedding = np.array(all_layer_embedding)[:, 4:, :, :]  # Start from 4th layers output

            embedding = []
            # One sentence at a time
            for sent_index in range(len(unmask_num)):
                sentence_feature = all_layer_embedding[sent_index, :, :unmask_num[sent_index], :]
                one_sentence_embedding = []
                # Process each token
                for token_index in range(sentence_feature.shape[1]):
                    token_feature = sentence_feature[:, token_index, :]
                    # 'Unified Word Representation'
                    token_embedding = unify_token(token_feature)
                    one_sentence_embedding.append(token_embedding)

                one_sentence_embedding = np.array(one_sentence_embedding)
                sentence_embedding = unify_sentence(sentence_feature, one_sentence_embedding)
                embedding.append(sentence_embedding)
            embedding = np.array(embedding)
            return embedding


def unify_token(token_feature, window_size=2):
    """
    Unify Token Representation
    """
    alpha_alignment = np.zeros(token_feature.shape[0])
    alpha_novelty = np.zeros(token_feature.shape[0])

    for k in range(token_feature.shape[0]):
        left_window = token_feature[k - window_size:k, :]
        right_window = token_feature[k + 1: k + window_size + 1, :]
        window_matrix = np.vstack([left_window, right_window, token_feature[k, :][None, :]])

        Q, R = np.linalg.qr(window_matrix.T)  # This gives negative weights

        q = Q[:, -1]
        r = R[:, -1]
        alpha_alignment[k] = np.mean(normalize(R[:-1, :-1], axis=0), axis=1).dot(R[:-1, -1]) / (np.linalg.norm(r[:-1]))
        alpha_alignment[k] = 1 / (alpha_alignment[k] * window_matrix.shape[0] * 2)
        alpha_novelty[k] = abs(r[-1]) / (np.linalg.norm(r))

    # Sum Norm
    alpha_alignment = alpha_alignment / np.sum(alpha_alignment)  # Normalization Choice
    alpha_novelty = alpha_novelty / np.sum(alpha_novelty)

    alpha = alpha_novelty + alpha_alignment

    alpha = alpha / np.sum(alpha)  # Normalize
    out_embedding = token_feature.T.dot(alpha)
    return out_embedding


def unify_sentence(sentence_feature, one_sentence_embedding):
    """
    Unify Sentence By Token Importance
    """
    sent_len = one_sentence_embedding.shape[0]

    var_token = np.zeros(sent_len)
    for token_index in range(sent_len):
        token_feature = sentence_feature[:, token_index, :]
        sim_map = cosine_similarity(token_feature)
        var_token[token_index] = np.var(sim_map.diagonal(-1))

    var_token = var_token / np.sum(var_token)
    sentence_embedding = one_sentence_embedding.T.dot(var_token)
    return sentence_embedding
