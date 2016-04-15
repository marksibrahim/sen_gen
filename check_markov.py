from tools import generate_sentence

class MarkovCheck():

    def __init__(self, our_story):
        self.story = our_story
        self.success = False

	def check_markov(self):
		while self.success == False:
			markov_sents = self.story.gen_sentences.generate_sents_w_noun(self.story.noun_prompt_obj.noun)[0]
			for sent in markov_sents:
				length = len(sent.split())
				if length <= 10:
					self.our_sent_1 = sent
					self.success = True
				else:
					self.success = False

		self.our_sent_1.replace('\"', '')
		self.our_sent_1.replace('\.', '')

		season = self.story.season['action2']
		air = "air"
		loneliness = "loneliness"
		fragile = "fragile"

		words = ['season', 'air', 'loneliness', 'fragile']
		word_prompt = random.choice(words)

		while self.success == False:
			markov_sents = self.story.gen_sentences.generate_sents_w_noun(word_prompt)[0]
			for sent in markov_sents:
				length = len(sent.split())
				if length <= 10:
					self.our_sent_2 = sent
					self.success = True
				else:
					self.success = False

		self.our_sent_2.replace('\"', '')
		self.our_sent_2.replace('\.', '')

		self.our_sentences = ['self.our_sent_1', 'self.our_sent_2']

		return self.our_sentences

