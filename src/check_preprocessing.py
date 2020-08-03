import re
from pprint import pprint

with open('../input/concat.txt','r') as f:
    text = f.read()
    found = re.findall(r'((?:<p>)?<s>[^<>]+</s>)+', text)
    print(len(found))
    pprint(found[:10])