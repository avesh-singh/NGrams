import re
from pprint import pprint

with open('../input/concat.txt','r') as f:
    text = f.read()
    found = re.findall(r'((?:<p>)?<s>[^<>]+</s>)+', text)
    print(len(found))
    pprint(found[:10])


with open('../input/unigram.txt','r') as f:
    words = f.read().split('\n')
    words = sorted(words)
    print([word for word in words if word.__contains__('--')])
