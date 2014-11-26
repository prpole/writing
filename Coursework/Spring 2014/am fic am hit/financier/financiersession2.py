# coding: utf-8
import nltk
help
help()
get_ipython().magic(u'quickref')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ../..')
get_ipython().magic(u'cd Columbia/Spring\\ 2014/')
get_ipython().magic(u'cd am\\ fic\\ am\\ hit/financier/')
get_ipython().system(u'ls -F -G ')
financier_session_one.py
get_ipython().magic(u'run financier_session_one.py')
open financier_session_one.py
get_ipython().magic(u'run financiertagged-bigramed.py')
get_ipython().magic(u'run financiertagged-bigramed.py')
financiertagged_pairs[100:200]
for w in financiertagged_pairs:
    if w[1] == ('eye', 'NN'):
        print financiertagged_pairs.index(w)
        
for (a, b) in financiertagged_pairs:
    if b[0] == 'eye':
        print financiertagged_pairs[(financiertagged_pairs.index((a, b))-4):(financiertagged_pairs.index((a, b))+4)]
        
for w in financiertagged:
    if w[0] == 'eye':
        print financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)]
    elif w[0] == 'eyes':
        print financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)]
        
eyesentstagged = []
for w in financiertagged:
    if w[0] == 'eye':
        eyesentstagged.append(financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)])
    elif w[0] == 'eyes':
        eyesentstagged.append(financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)])
        
eyesentstagged
eyesentstaggedfile = open('eyesentstagged.txt', 'w')
eyesentstaggedfile.write(eyesentstagged)
eyesentstaggedfile.write(str(eyesentstagged))
eyesentstaggedfile.close()
for w in financiertagged:
    if w[0] == 'eye':
        eyesentstagged.append(financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)])
    elif w[0] == 'eyes':
        eyesentstagged.append(financiertagged[(financiertagged.index(w)-4):(financiertagged.index(w)+4)])
        
for w in financiertagged:
    if w[0] == 'eye':
        print financiertagged.index(w)
    elif w[0] == 'eyes':
        print financiertagged.index(w)
        
for w in financiertagged:
    if w[0] == 'eye':
        print financiertagged.index(w)
    elif w[0] == 'eyes':
        print financiertagged.index(w)
        
eyeindices = []
for w in financiertagged:
    if w[0] == 'eye':
        eyeindices.append(financiertagged.index(w))
    elif w[0] == 'eyes':
        eyeindices.append(financiertagged.index(w))
        
set(eyeindices)
financierset = set(financiertagged)
financierset
fncrtext = nltk.text.Text(tokens)
fncrtext
fncrtext.plot
fncrtext.findall('eye')
get_ipython().magic(u'pinfo fncrtext.findall')
fncrtext.findall('<eye>')
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
fncrsents = sent_tokenizer.tokenize(raw)
fncrsents[1:20]
sentstoked = nltk.word_tokenize(fncrsents)
sent_tokenizer.sentences_from_tokens(tokens)
fncrsents = sent_tokenizer.sentences_from_tokens(tokens)
fncrsents(1:10)
fncrsents[1:10]
fincrsents
fncrsents
get_ipython().magic(u'pinfo tokens')
get_ipython().magic(u'pinfo sent_tokenizer.sentences_from_tokens')
tokens
tokens[1:10]
fncrtokens = tokens
fncrsents
fncrsents = sent_tokenizer.sentences_from_tokens(fncrtokens)
fncrsents
get_ipython().magic(u'pinfo fncrsents')
fncrsents = sent_tokenizer.sentences_from_tokens(raw)
fncrsents
fncrsents
fncrsents = sent_tokenizer.tokenize(raw)
fncrsents
eyesents = []
get_ipython().magic(u'pinfo fncrsents')
for w in fncrsents:
    if re.search('^eye$', w):
        eyesents.append(w)
        
import re
for w in fncrsents:
    if re.search('^eye$', w):
        eyesents.append(w)
        
eyesents
for w in fncrsents:
    if re.search('eye', w):
        print w
        
for w in fncrsents:
    if re.search('eye', w):
        eyesents.append(w)
        
eyesents
for w in eyesents:
    nltk.word_tokenize(w)
    
eyesents
for w in eyesents:
    wnew = nltk.word_tokenize(w)
    print wnew
    
for w in eyesents:
    wnew = nltk.word_tokenize(w)
    eyesents.append(wnew)
    eyesents.remove(w)
    
for w in eyesents:
    wnew = nltk.word_tokenize(w)
    eyesents.append(wnew)
    
[a[1] for (a, b) in financiertagged if b[1] == 'NN'] 
financiertagged[:10]
[b for (a, b) in financiertagged if b[1] == 'NN']
[a[1] for (a, b) in financiertagged_pairs if b[1] == 'NN']
nounmodcfd = nltk.ConditionalFreqDist(

)
nounmod = [a[1] for (a, b) in financiertagged_pairs if b[1] == 'NN']
nounmodcfd = nltk.ConditionalFreqDist(nounmod)
nltk.ConditionalFreqDist
get_ipython().magic(u'pinfo nltk.ConditionalFreqDist')
nounmodfd = nltk.FreqDist(nounmod)
nounmodfd.tabulate()
nounmodfd.plot()
eye_fd
eyes_fd
eye_fd.tabulate()
eyes_fd.tabulate()
eyesents
get_ipython().magic(u'save financiersession2 1-95')
