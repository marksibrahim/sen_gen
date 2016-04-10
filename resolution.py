
# coding: utf-8

# In[2]:

"""
generates Resolution, which is comprised of paragraph 22, based on elements in story.py

"""

import random

class Resolution():

    def __init__(self, our_story):
        self.story = our_story

    def gen_par22(self):
        
        # But < I > knew it couldn't be. < I > know it can't be.

        s1 = "But " + self.story.ch3['pronoun'] + " knew it couldn't be. " +              self.story.ch3['pronoun'] + " know it can't be."
        
        # The < stone > < box > sits on < my > < bookshelf > and is always < cool >.
        s2 = "The " + self.story.symbol_adj + " " + self.story.symbol_n +              " sits on " + self.story.ch3['possessive'] + " " + self.story.symbol_addtl_n +              " and is always " + self.story.symbol_adj_temp + "."
        
        # It's < heavy > and < light > at the same time.  
        
        s3 = "It's " + self.story.symbol_adj_weight + " and " +              self.story.symbol_adj_weight_opposite + " at the same time."
        
        # When < I > hold it, < I > feel < hopeful > .

        s4 = "When " + self.story.ch3['pronoun'] + " hold it, " + self.story.ch3['pronoun'] +              " feel " + self.story.resolution_adj + "."
        
        p22 = s1 + " " + s2 + " " + s3 + " " + s4
        
        return p22
    
    def gen_action6(self):
                  
        resolution = self.gen_par22()

        return resolution

