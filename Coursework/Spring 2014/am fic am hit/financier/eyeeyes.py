import nltk

file = open('eye eyes instances.md', 'r+')
raw = file.read()
tokens = nltk.word_tokenize(raw)
tagged = nltk.pos_tag(tokens)
word_tag_pairs = nltk.bigrams(tagged)