from os.path import isfile
import src.prepare_text as prepare

def get_unigrams():
    if isfile('../input/unigram.txt'):
        f = open('../input/unigram.txt','r')
        return f.read().split('\n')
    if isfile('../input/concat.txt'):
        with open('../input/concat.txt') as f:
            return f.read().split(' ')
    text = prepare.prepare_text()
    # unigram
    unigram = text.split(' ')
    with open('../input/unigram.txt', 'w') as g:
        for item in unigram:
            g.write('%s\n' % item)
    return unigram


def get_bigrams():
    unigram = get_unigrams()
    bigram = []
    for i in range(1, len(unigram)):
        bigram.append('{} {}'.format(unigram[i - 1], unigram[i]))
    return bigram

def get_trigrams():
    unigram = get_unigrams()
    trigram = []
    for i in range(2, len(unigram)):
        trigram.append('{} {} {}'.format(unigram[i - 2], unigram[i - 1], unigram[i]))
    return trigram

def get_quadgrams():
    unigram = get_unigrams()
    quadgram = []
    for i in range(3, len(unigram)):
        quadgram.append('{} {} {} {}'.format(unigram[i - 3], unigram[i - 2], unigram[i - 1], unigram[i]))
    return quadgram