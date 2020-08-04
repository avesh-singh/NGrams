from src import ngrams
from random import uniform
from math import ceil

# sampling from quadgrams list directly
def generate_sentence():
    quadgrams = ngrams.get_quadgrams()
    sentence = []
    first_word = ''
    first_quadgram = ''
    counter = 0
    while first_word != '<s>' and first_word != '<p>':
        counter += 1
        pick = ceil(uniform(0, len(quadgrams) - 1))
        first_quadgram = quadgrams[pick]
        first_word = first_quadgram.split(' ')[0]
    print('[%d]'%counter)
    sentence.extend(first_quadgram.split(' '))
    print(sentence)
    last_trigram = ' '.join(sentence[1:])
    last_word = ''
    while last_word != '</s>' and last_word != '</p>':
        counter += 1
        pick = ceil(uniform(0, len(quadgrams) - 1))
        phrase = quadgrams[pick]
        print(phrase)
        words = phrase.split(' ')
        if ' '.join(words[1:]) != last_trigram:
            continue
        # print('[%d]'%counter)
        # print(sentence)
        last_word = words[-1]
        sentence.append(words[-1])
        words.pop(0)
        last_trigram = ' '.join(words)
    return ' '.join(sentence),counter

