from nltk import tokenize

import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = sys.argv[1]

cmd ='java -jar ContentExtracter.jar '+ '"' + url + '"'

print cmd

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
content = ' '.join(p.stdout.readlines())

from nltk.tag import StanfordNERTagger

st = StanfordNERTagger('/home/harsha/.install/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz','/home/harsha/.install/stanford-ner-2016-10-31/stanford-ner.jar')

d = {'LOCATION':[],'ORGANIZATION':[],'PERSON':[]}

for sentence in tokenize.sent_tokenize(content):
    print sentence
    tagged_words = [t for t in st.tag(sentence.split()) if t[1] != 'O']
    print tagged_words

    # print tagged_words

    temp = None 
    last_type = None
    for word,tag in tagged_words:
        if not temp:
            # New run
            temp = [word]
            last_type = tag
        elif last_type == tag:
            # Extend the phrase
            temp.append(word)
        else:
            print temp 
            d[last_type].append(' '.join(temp))
            temp = [word]
            last_type = tag

    if temp:
        print temp
        d[last_type].append(' '.join(temp))

    print '----------------------------'

for k in d:
    print '----------'
    print (k)
    print '----------'
    for v in d[k]:
        print v
