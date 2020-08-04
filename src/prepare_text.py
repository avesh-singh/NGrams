import re
import os


def prepare_text():
    global files, filename, text
    concat_text = ""
    open('../input/concat.txt', 'w').close()
    for dir, subdir, files in os.walk('../input'):
        files.sort()
        if 'concat.txt' in files:
            files.remove('concat.txt')
        if 'unigram.txt' in files:
            files.remove('unigram.txt')
        for filename in files:
            print(filename)
            with open('{}/{}'.format(dir, filename), 'r') as f:
                text = f.read()
                concat_text += '<s1> '
                text = re.sub(r'(.*:)\s\s', '', text)
                text = re.sub('.\n\n', ' </s1>\n<s1> ', text)
                text = re.sub('\n', ' ', text)
                text = re.sub(r'(St)\.\s(\w+)', r'\1-\2', text)
                text = re.sub(r'(\d)\.(\d)', r'\1,\2', text)
                text = re.sub('[!?]',r'.',text)
                text = re.sub(r'(\s?)(?!St\.)\b(\w+)\.(\s?)', r'\1\2 </s1>\3<s1> ', text)
                text = re.sub(r'<s1>(?!.*</s1>)', '', text)
                text = re.sub('(\d|\w),(?!\d)', r'\1', text)
                text = re.sub('[;",]','',text)
                text = re.sub('--', ' ', text)
                concat_text += text + ' \n\n'
    with open('../input/concat.txt', 'w') as f:
        f.write(concat_text.lower())
    return concat_text

prepare_text()

