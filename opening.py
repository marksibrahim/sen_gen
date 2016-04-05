"""
generates first paragraph based on elements in story.py
"""

import random
from nltk.corpus import wordnet as wn

#create story instance to use in generation of first paragraph


class Opening():
    """
    drafts first paragraph based on elemnts in 
    instance of story provided
    """
    def __init__(self, our_story):
        self.story = our_story
        seasons = ['hot summer', 'cold winter', 'rainy spring', 'crisp fall']
        self.season = random.choice(seasons)
        self.grass = 'They sat on the grass in the open air, thinking this would be a day to remember.'
        self.cafe = 'They sat huddled around a warm cup of coffee, thinking this would be a day to remember.'
        self.setting_description = {
                'hot summer': self.grass,
                'rainy spring': self.grass,
                'crisp fall': self.cafe,
                'cold winter': self.cafe
                }
        #test variable
        self.story.test_var = 17

    def gen_meeting(self):
        """
        characters meet in setting
        s1 = June and Charlie met on a summer day.
        s2 = 
        """
        s1 = self.story.characters[0][0] + " and " + self.story.characters[1][0]
        s1 += " met on a "  + self.season + " day."
        s2 = self.setting_description[self.season]
        return s1 + " " + s2

    def tell_children(self):
        """
        characters tell children about the air that day
        """
        #tell = [w.lemma_name for w in wn.synsets('tell')]
        s3 = "They would" + "tell" + "their children about the "
        s3 += self.season + " air the day they met."
        s4 = "They just knew."
        return s3 + " " + s4

    def draft(self):
        return  self.gen_meeting() + self.tell_children()

