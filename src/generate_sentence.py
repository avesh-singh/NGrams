from src import bigram,trigram,quadgram
import time

start_time = time.time()
print(quadgram.generate_sentence())
print('%s seconds' % (time.time() - start_time))

#
# start_time = time.time()
# print(bigram.generate_sentence_naive_filtered())
# print('%s seconds' % (time.time() - start_time))