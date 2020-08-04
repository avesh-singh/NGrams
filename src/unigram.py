from src import ngrams
from random import uniform
from math import ceil


def generate_sentence():
    unigrams = ngrams.get_unigrams()
    sentence = []
    first_word = ''
    counter = 0
    while first_word != '<s1>':
        counter += 1
        pick = ceil(uniform(0, len(unigrams) - 1))
        first_word = unigrams[pick]
    sentence.append(first_word)
    word = ''
    while word != '</s1>':
        counter += 1
        pick = ceil(uniform(0, len(unigrams) - 1))
        word = unigrams[pick]
        if word == '<s1>':
            continue
        sentence.append(word)
    return ' '.join(sentence), counter
