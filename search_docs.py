from functools import wraps

import numpy as np
from numpy.linalg import norm
import pandas as pd


__all__ = ['search_docs']


def validate_searched_txt(callback):
    @wraps(callback)
    def validate(searched_txt, docs_to_search):
        if searched_txt == '':
            return pd.DataFrame(data=docs_to_search, columns=['All Documents']), None, None

        query = searched_txt.strip()
        if query == '':
            return pd.DataFrame(), None, None

        return callback(query, docs_to_search)
    return validate


@validate_searched_txt
def search_docs(query, docs_to_search):
    all_docs = [query] + docs_to_search

    words = find_unique_words(all_docs)
    frequency_mat = get_frequency_mat(all_docs, words)
    weights_mat = calc_weights(frequency_mat, all_docs, words)

    similarity = find_cosine_similarity(weights_mat.iloc[0], weights_mat.iloc[1:])

    results = pd.DataFrame(data=np.array([docs_to_search, similarity]).T, columns=['Documents', 'Matching'])
    results = results.sort_values(by='Matching', ascending=False)
    
    return results, frequency_mat, weights_mat


def find_unique_words(docs):
    words = ' '.join(docs).split()
    unique_words = list(set(words))

    return unique_words


def get_frequency_mat(docs, words):
    frequency_mat = pd.DataFrame(columns=words)

    for d, doc in enumerate(docs):
        frequency_mat.loc[d] = pd.Series(
            data=[doc.split().count(word) for word in words],
            index=words
        )

    return frequency_mat


def calc_weights(frequency_mat, docs, words):
    weights_mat = pd.DataFrame(columns=words)
    no_of_docs = frequency_mat.shape[0]

    dfi = (frequency_mat>0).sum()
    idf = np.log2(dfi.apply(lambda df: no_of_docs/df))

    for i, doc in frequency_mat.iterrows():
        tfd = doc.apply(lambda word: word/doc.max())
        weights_mat.loc[i] = tfd*idf

    return weights_mat


def find_cosine_similarity(query, docs):
    return [np.inner(query, doc)/(norm(query)*norm(doc))
     for _, doc in docs.iterrows()]
