from os.path import isfile
import src.prepare_text as prepare
import sys

def get_unigrams():
    if isfile('../input/unigram.txt'):
        f = open('../input/unigram.txt','r')
        return f.read().split('\n')
    if isfile('../input/concat.txt'):
        with open('../input/concat.txt','r') as f:
            text = f.read()
    else:
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
    for i in range(len(unigram)):
        if unigram[i] == '<s1>':
            print(unigram[i:i+3])
            unigram[i:i + 1] = '<s1>','<s2>'
            i += 1
            print(unigram[i:i + 3])
        elif unigram[i] == '</s1>':
            print(unigram[i:i + 3])
            unigram[i:i + 1] = '</s2>', '</s1>'
            i += 1
            print(unigram[i:i + 3])
    trigram = []
    for i in range(2, len(unigram)):
        trigram.append('{} {} {}'.format(unigram[i - 2], unigram[i - 1], unigram[i]))
    return trigram

def get_quadgrams():
    unigram = get_unigrams()
    for i in range(len(unigram)):
        if unigram[i] == '<s1>':
            unigram[i:i + 1] = '<s1>','<s2>','<s3>'
            i += 2
        elif unigram[i] == '</s1>':
            unigram[i:i + 1] = '</s3>','</s2>', '</s1>'
            i += 2
    quadgram = []
    for i in range(3, len(unigram)):
        quadgram.append('{} {} {} {}'.format(unigram[i - 3], unigram[i - 2], unigram[i - 1], unigram[i]))
    return quadgram

if __name__ == '__main__':
    if '1' in sys.argv:
        print('generating unigrams')
        print(get_unigrams()[:40])
    if '2' in sys.argv:
        print('generating bigrams')
        print(get_bigrams()[:40])
    if '3' in sys.argv:
        print('generating trigrams')
        print(get_trigrams()[:40])
    if '4' in sys.argv:
        print('generating quadgrams')
        print(get_quadgrams()[:40])
