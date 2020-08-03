from src import ngrams
from random import uniform
from math import ceil


def generate_sentence():
    unigrams = ngrams.get_unigrams()
    sentence = []
    first_word = ''
    while first_word != '<s>' and first_word != '<p>':
        pick = ceil(uniform(0, len(unigrams) - 1))
        first_word = unigrams[pick]
    sentence.append(first_word)
    word = ''
    while word != '</s>' and word != '</p>':
        pick = ceil(uniform(0, len(unigrams) - 1))
        word = unigrams[pick]
        if word == '<s>' or word == '<p>':
            continue
        sentence.append(word)
    return ' '.join(sentence)
