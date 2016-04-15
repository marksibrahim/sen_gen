"""
authors a short story based on a noun prompt
"""

import sys
import random
import action1, action2, action3, action4, action5, action6, action7, action8, action9
from tools import characters, generate_sentence, story_pieces

from nltk.corpus import wordnet as wn
from nltk import word_tokenize
import nltk

class Story():

    def __init__(self, noun_prompt):
        """
        global variables for our story
        """
        self.noun_prompt = noun_prompt
        self.noun_prompt_obj = Noun_Prompt(noun_prompt)

        story_type = ["1", "2"]
        self.story_type = random.choice(story_type)
        
        # HERE, WE NEED TO PARSE OUT NOUN PROMPT AND ASSIGN STORY CATEGORY

        # generate character and story pieces based on noun prompt
        self.gen_character(self.story_type)
        self.gen_story_pieces(self.story_type)

        #instantiate markov sentence generator
            # to use call method: generate_sents_w_noun("dog")
        self.gen_sentences = generate_sentence.Sentences()


    def gen_character(self, story_type):
        """
        creates character dictionary with first name, gender and all pronouns;
        takes a story type to know how many characters to create
        """

        self.story_type = story_type

        # for generating a random gender & pov where indicated
        g = ['male', 'female']
        p = ['first', 'third']

        if self.story_type == "1" or self.story_type == "2":
            # generate 4 characters; takes: gender, pov, plural

            gender = random.choice(g)
            ch = characters.Character(gender, 'third', False)
            self.ch1 = ch.create_character()

            gender = random.choice(g)
            ch = characters.Character(gender, 'third', False)
            self.ch2 = ch.create_character()

            gender = random.choice(g)
            pov = random.choice(p)
            ch = characters.Character(gender, pov, False)
            self.ch3 = ch.create_character()

            gender = random.choice(g)
            ch = characters.Character(gender, 'third', False)
            self.ch4 = ch.create_character()


    def gen_story_pieces(self, story_type):
        """
        creates seasons, settings, places, theme pieces, symbols, actions;
        takes a story type to know theme
        """
        self.season = story_pieces.gen_seasons() 
        self.setting_sAB = story_pieces.gen_setting_sentences()
        self.event = story_pieces.gen_event(story_type)
        self.theme = story_pieces.gen_theme(story_type)
        self.symbol = story_pieces.gen_symbols(story_type)
        self.a1_surprise = story_pieces.gen_action1_and_surprise(story_type)


    def author_story(self):
        """
        calls section modules to create story
        """

        self.action1 = action1.Action1(self).gen_action1()
        self.action2 = action2.Action2(self).gen_action2()
        self.action3 = action3.Action3(self).gen_action3()
        self.action4 = action4.Action4(self).gen_action4()
        self.action5 = action5.Action5(self).gen_action5()
        self.action6 = action6.Action6(self).gen_action6() 
        self.action7 = action7.Action7(self).gen_action7()
        self.action8 = action8.Action8(self).gen_action8()
        self.action9 = action9.Action9(self).gen_action9()


        return self.action1 + "\n\n" + self.action2 + "\n\n" + self.action3 + "\n\n" + self.action4 + \
               "\n\n" + self.action5 + "\n\n" + self.action6 + "\n\n" + self.action7 + "\n\n" + \
               self.action8 + "\n\n" + self.action9

class Noun_Prompt():
    """
    stores and processes given noun_prompt
    """
    def __init__(self, noun_prompt):
        self.noun_prompt = noun_prompt

        self.category = self.categorize(self.noun_prompt)
        self.abstraction = self.check_abstraction()
        
        self.noun = noun_prompt
        self.adj = []
        self.check_adj()

    def check_abstraction(self):
        """
        checks whether noun prompt is abstraction
        """
        try:
            if "abstraction" in self.category:
                return True
            else:
                return False
        except TypeError:
            return False

    def categorize(self, noun, level=1):
        """
        returns a category for the given noun
        """
        try: 
          noun_syns = wn.synsets(noun, 'n')[0]
          category = noun_syns.hypernym_paths()[0][level]
          return category.name()
        except IndexError:
          return False

    def check_adj(self):
        """
        if noun isn't categorized, function attempts to 
        split into adj and noun parts
        """
        if self.category: 
            return False
        else:
            text = word_tokenize(self.noun_prompt)
            self.adj = []
            for i, w in enumerate(nltk.pos_tag(text)):
                if "JJ" in w[1]:
                    self.adj.append(w[0])
                else:
                    self.noun = w[0]
        try:
            self.category = self.categorize(self.noun)
            self.abstraction = self.check_abstraction(self)
        except:
            self.abstraction = False
            self.category = False


if __name__ == "__main__":
    try:
        noun_prompt = sys.argv[1:][0]
        our_story = Story(noun_prompt)
        print(our_story.author_story())
    except:
        try:
            noun_prompt = sys.argv[1:][0]
            our_story = Story(noun_prompt)
            print(our_story.author_story())
        except:
            noun_prompt = sys.argv[1:][0]
            our_story = Story(noun_prompt)
            print(our_story.author_story())
