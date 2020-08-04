from src import ngrams
from random import uniform
from math import ceil

# sampling from bigrams list directly
def generate_sentence():
    bigrams = ngrams.get_bigrams()
    sentence = []
    first_word = ''
    first_phrase = ''
    counter = 0
    while first_word != '<s1>':
        counter += 1
        pick = ceil(uniform(0, len(bigrams) - 1))
        first_phrase = bigrams[pick]
        first_word = first_phrase.split(' ')[0]
    sentence.extend(first_phrase.split(' '))
    last_word = sentence[-1]
    while last_word != '</s1>':
        counter += 1
        pick = ceil(uniform(0, len(bigrams) - 1))
        phrase = bigrams[pick]
        word_one,word_two = phrase.split(' ')
        if word_one != last_word:
            continue
        last_word = word_two
        sentence.append(word_two)
    return ' '.join(sentence), counter

# generating from filtered list
def generate_sentence_naive_filtered():
    bigrams = ngrams.get_bigrams()
    sentence = []
    first_word = ''
    first_phrase = ''
    counter = 0
    filtered_bigrams = [phrase for phrase in bigrams if phrase[:3] == '<s1>']
    while first_word != '<s1>':
        counter += 1
        pick = ceil(uniform(0, len(filtered_bigrams) - 1))
        first_phrase = filtered_bigrams[pick]
        first_word = first_phrase.split(' ')[0]
    print('[%d]' % counter)
    sentence.extend(first_phrase.split(' '))
    last_word = sentence[-1]
    filtered_bigrams = [phrase for phrase in bigrams if phrase.split(' ')[0] == last_word]
    while last_word != '</s1>':
        counter += 1
        pick = ceil(uniform(0, len(filtered_bigrams) - 1))
        phrase = filtered_bigrams[pick]
        word_one, word_two = phrase.split(' ')
        if word_one != last_word:
            continue
        print('[%d]' % counter)
        last_word = word_two
        sentence.append(word_two)
        filtered_bigrams = [phrase for phrase in bigrams if phrase.split(' ')[0] == last_word]
    return ' '.join(sentence),counter

