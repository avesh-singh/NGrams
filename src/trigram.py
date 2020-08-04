from src import ngrams
from random import uniform
from math import ceil

# sampling from trigrams list directly
def generate_sentence():
    trigrams = ngrams.get_trigrams()
    sentence = []
    first_word = ''
    first_trigram = ''
    counter = 0
    while first_word != '<s1>':
        counter += 1
        pick = ceil(uniform(0, len(trigrams) - 1))
        first_trigram = trigrams[pick]
        first_word = first_trigram.split(' ')[0]
    sentence.extend(first_trigram.split(' '))
    last_bigram = ' '.join(sentence[-2:])
    last_word = ''
    while last_word != '</s1>' or last_word != '</s2>':
        counter += 1
        pick = ceil(uniform(0, len(trigrams) - 1))
        phrase = trigrams[pick]
        word_one,word_two,word_three = phrase.split(' ')
        if "{} {}".format(word_one,word_two) != last_bigram:
            continue
        last_word = word_three
        last_bigram = ' '.join([word_two,word_three])
        sentence.append(word_three)
    return ' '.join(sentence),counter

