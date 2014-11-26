# coding: utf-8
import eyeeyes
eyeeyes.word_tag_pairs
import nltk
list(nltk.FreqDist(a[1] for (a, b) in eyeeyes.word_tag_pairs if b[0] == 'eye'))
eye_fd = nltk.FreqDist(a[1] for (a, b) in eyeeyes.word_tag_pairs if b[0]== 'eye')
eye_fd.tabulate()
eyes_fd = nltk.FreqDist(a[1] for (a, b) in eyeeyes.word_tag_pairs if b[0] == 'eyes')
eyes_fd.tabulate()

words_w_ndx = [(w, eyeeyes.tagged.index(w)) for w in eyeeyes.tagged]
eyeeyes.word_tag_pairs
eye_indices = [eyeeyes.word_tag_pairs.index((a, b)) for (a, b) in eyeeyes.word_tag_pairs if b[0] == 'eye']