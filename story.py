"""
authors a short story based on a theme
"""

import random
from nltk.corpus import names

import opening, action1, action2

from tools import generate_sentence

class Story():
    """
    theme
        contains opening, conflict, resolution
    characters
        name + gender, units: family
    setting
    """

    def __init__(self, noun_prompt):
        """
        global variables for our story
        """
        self.noun_prompt = noun_prompt
        self.narrator = "I"
        self.characters = [ self.gen_character("male"), 
                            self.gen_character("female"),
                            self.narrator, 
                            self.gen_character("female"),
                            self.gen_character("male"), 
                            ]
        self.theme =  "love"
        #instantiate markov sentence generator
            # to use call method: generate_sents_w_noun("dog")
        self.gen_sentences = generate_sentence.Sentences()

    def gen_character(self, gender):
        """
        returns a character name based given gender
        """
        if gender == "male":
            name = random.choice([(name) for name in names.words('male.txt')])
            pronoun = "he"
        else:
            name = random.choice([(name) for name in names.words('female.txt')])
            pronoun = "she"

        return name, pronoun

    def return_possesive(self, gender, pov, plural=False):
        """
        returns possessive based on gender and number
        pov is point of view: 
            first person, second person, third person, and it
        e.g, return_possessive("male", "third", plural=True)
        """
        pass

    def author_story(self):
        """
        calls par modules to create story
        """
        self.opening = opening.Opening(self).draft()
        self.action1 = action1.Action1(self).draft()
        self.action2 = action2.Action2(self).draft()
        return self.opening + "\n" + self.action1


if __name__ == "__main__":
    our_story = Story("dog")
    print(our_story.author_story())
