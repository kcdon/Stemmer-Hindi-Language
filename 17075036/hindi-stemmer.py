#suffix stripping algorithm for implementing a stemmer in Hindi language inspired from Porter Stemmer

#installing dependencies
import codecs
import re

#read the input file
filepath = 'hindi.txt'
f = codecs.open(filepath, encoding = 'utf-8')
text = f.read()


sentences=text.split(u"।") #since hindi sentences end with '|'
words_list = list()
for sentence in sentences:
    words = sentence.split(' ') #words are seperated by a space in hindi
    words_list += words

suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
} #suffixes tin hindi language that change tense, gender, number but not the meaning

stems=[]
for word in words_list:
    for L in 5, 4, 3, 2, 1:
        if len(word) >= L + 1:
            for suffix in suffixes[L]:
                if word.endswith(suffix):
                    word=word[:-L] #stripping the suffix from the word
    if word:
        stems.append(word)

filename='stems_generated.txt'
f=codecs.open(filename,"w",encoding='utf-8') #open in write mode
for stem in stems:
    f.write(str(stem))
    f.write(u"\u0020")
f.close()
