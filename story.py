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



            

        
        


