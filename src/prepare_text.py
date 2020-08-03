import re
import os


def prepare_text():
    global files, filename, text
    concat_text = ""
    open('../input/concat.txt', 'w').close()
    for dir, subdir, files in os.walk('../input'):
        files.sort()
        files.remove('concat.txt')
        for filename in files:
            print(filename)
            with open('{}/{}'.format(dir, filename), 'r') as f:
                text = f.read()
                concat_text += '<p> <s> '
                text = re.sub(r'(.*:)\s\s', '', text)
                text = re.sub('.\n\n', ' </s> </p>\n<p> <s>', text)
                text = re.sub('\n', ' ', text)
                text = re.sub(r'(St)\.\s(\w+)', r'\1-\2', text)
                text = re.sub(r'(\d)\.(\d)', r'\1,\2', text)
                text = re.sub('[!?]',r'.',text)
                text = re.sub(r'(\s?)(?!St\.)\b(\w+)\.(\s?)', r'\1\2 </s>\3<s> ', text)
                text = re.sub(r'<s>(?!.*</s>)', '', text)
                text = re.sub('(\d|\w),(?!\d)', r'\1', text)
                text = re.sub('[;",]','',text)
                # print(re.findall('\sFoxesetc\s?', text))
                concat_text += text + ' </p>\n\n'
    with open('../input/concat.txt', 'w') as f:
        f.write(concat_text.lower())
    return concat_text

prepare_text()
