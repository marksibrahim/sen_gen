"""
authors a short story
based on generated sentences
"""

import markov
from nltk.tokenize import sent_tokenize

corpus_path = "clean/all_utf-8.txt"

class Story():

    def __init__(self):
        with open(corpus_path, encoding="utf-8") as corp:
            self.markov_generator = markov.Markov(corp)
    
    def generate_sentence(self):
        """
        generates a sentence based on short story corpus 
        requires markov.py
        """
        raw_sen_text = self.markov_generator.generate_markov_text(size=200)
        sentence_list = sent_tokenize(raw_sen_text)
        sentence_list.pop(0)
        sentence_list.pop()

        return sentence_list[0]


    def generate_sents_w_noun(self, noun, num=1):
        """
        generates the given number of sentences with the given noun
        returns a list of sentences
        """
        sentences = [] 
        for i in range(num*100):
            sent = self.generate_sentence()
            if noun in sent:
                sentences.append(sent)
            #exit if enough sentences are generated
            if len(sentences) > num:
                break
        return sentences



        #!/usr/bin/env python3
# encoding: utf-8
 
import sys
from pprint import pprint
from random import choice
 
EOS = ['.', '?', '!']
 
 
def build_dict(words):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in d:
            d[key] = []
        #
        d[key].append(third)
 
    return d
 
 
def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
 
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key
 
    return ' '.join(li)
 
 
def main():
    fname = sys.argv[1]
    with open(fname, "rt", encoding="utf-8") as f:
        text = f.read()
 
    words = text.split()
    d = build_dict(words)
    pprint(d)
    print()
    sent = generate_sentence(d)
    print(sent)
    if sent in text:
        print('# existing sentence :(')
 
####################
 
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: provide an input corpus file.")
        sys.exit(1)
    # else
    main()    

        
        


