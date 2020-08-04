from src import unigram,bigram,trigram,quadgram
import time
import sys

def generate(ngram: str):
    if ngram == '1':
        ngrams = unigram
    elif ngram == '2':
        ngrams = bigram
    elif ngram == '3':
        ngrams = trigram
    elif ngram == '4':
        ngrams = quadgram
    else:
        raise ValueError('"%s" is not a valid length of n-gram'%ngram)
    start_time = time.time()
    print(ngrams.generate_sentence())
    print('%s seconds' % (time.time() - start_time))

if __name__ == '__main__':
    # run this file with multiple arguments for eg "generate_sentence 1 2 3 4"
    args = sys.argv[1:]
    print(args)
    for arg in args:
        generate(arg)
