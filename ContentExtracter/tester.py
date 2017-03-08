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


for sentence in tokenize.sent_tokenize(content):
    print sentence
    print '----------------------------'
