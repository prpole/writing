# coding: utf-8
import nltk
import eyeeyes
import financier_session_one
import urllib
from urllib import urlopen
url = "http://www.gutenberg.org/cache/epub/1840/pg1840.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
raw = raw[621:1114838]
tokens = nltk.word_tokenize(raw)
financiertagged = nltk.pos_tag(tokens)
financiertagged_pairs = nltk.bigrams(financiertagged)

