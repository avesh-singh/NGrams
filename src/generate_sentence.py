from src import unigram,bigram,trigram,quadgram
import time
import sys

def generate(ngram: str):
    ngrams = None
    if ngram == '1':
        ngrams = unigram
    elif ngram == '2':
        ngrams = bigram
    elif ngram == '3':
        ngrams = trigram
    elif ngram == '4':
        ngrams = quadgram
    start_time = time.time()
    print(ngrams.generate_sentence())
    print('%s seconds' % (time.time() - start_time))

if __name__ == '__main__':
    generate(sys.argv[1])
