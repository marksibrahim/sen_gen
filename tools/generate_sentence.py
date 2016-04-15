"""
authors a short story
based on generated sentences
"""

import random
from nltk.tokenize import sent_tokenize

corpus_path = "clean/all_utf-8.txt"
alternate_path = "tools/clean/all_utf-8.txt"

class Sentences():

    def __init__(self):
        try:
            with open(corpus_path, encoding="utf-8") as corp:
                self.markov_generator = Markov(corp)
        except FileNotFoundError:
            with open(alternate_path, encoding="utf-8") as corp:
                self.markov_generator = Markov(corp)

    
    def generate_sentence(self):
        """
        generates a sentence based on short story corpus 
        """
        raw_sen_text = self.markov_generator.generate_markov_text(size=200)
        sentence_list = sent_tokenize(raw_sen_text)
        sentence_list.pop(0)
        #return all except the last sentence
        return sentence_list[:-1]


    def generate_sents_w_noun(self, noun, num=5):
        """
        generates the given number of sentences with the given noun
        returns a list of sentences
        """
        sentences = [] 
        for i in range(num*800):
            sents = self.generate_sentence()
            for sent in sents:
                if noun in sent:
                    sentences.append(sent)
            #exit if enough sentences are generated
            if len(sentences) > num:
                break
        return sentences

    def generate_sents_w_many_nouns(self, nouns, num=2):
        sentences = [] 
        for i in range(num*2500):
            sents = self.generate_sentence()
            for sent in sents:
                found = True
                for noun in nouns:
                    if noun not in sent:
                        found = False
                        break
                if found:
                    sentences.append(sent)
            #exit if enough sentences are generated
            if len(sentences) > num:
                break
        return sentences


class Markov(object):

# implementation from gist: https://gist.github.com/dellis23/6174914
	def __init__(self, open_file, chain_size=3):
		self.chain_size = chain_size
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()

	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words

	def words_at_position(self, i):
		"""Uses the chain size to find a list of the words at an index."""
		chain = []
		for chain_index in range(0, self.chain_size):
			chain.append(self.words[i + chain_index])
		return chain

	def chains(self):
		"""Generates chains from the given data string based on passed chain size.

		So if our string were:
			"What a lovely day"

		With a chain size of 3, we'd generate:
			(What, a, lovely)
		and
			(a, lovely, day)
		"""

		if len(self.words) < self.chain_size:
			return

		for i in range(len(self.words) - self.chain_size - 1):
			yield tuple(self.words_at_position(i))

	def database(self):
		for chain_set in self.chains():
			key = chain_set[:self.chain_size - 1]
			next_word = chain_set[-1]
			if key in self.cache:
				self.cache[key].append(next_word)
			else:
				self.cache[key] = [next_word]

	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size - 3)
		gen_words = []
		seed_words = self.words_at_position(seed)[:-1]
		gen_words.extend(seed_words)
		for i in range(size):
			last_word_len = self.chain_size - 1
			last_words = gen_words[-1 * last_word_len:]
			next_word = random.choice(self.cache[tuple(last_words)])
			gen_words.append(next_word)
		return ' '.join(gen_words)
