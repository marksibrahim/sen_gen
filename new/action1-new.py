
# coding: utf-8

# In[ ]:

import random
from collections import defaultdict

class Action1():    
    """
    generates Action 1 (opening), which is comprised of paragraph 1, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story
        
        # s1
        self.protags = self.story.ch1['first_name'] + " and " + self.story.ch2['first_name']
        self.action = "met"

        # s3
        self.moment = "day"
        self.reaction = "remember"
        
        # s4
        self.relations = "children"
        

    def gen_par1(self):  

        # s1 < June and Charlie > < met > on a < summer > < day >.
        s1 = self.protags + " " + self.action + " on a " + self.story.season['action1'] + " day."

        # s2 < It was so hot the grass was laying down yellow in exhaustion > and 
        #    < the air was so heavy it was hard to breath >.
        
        season = self.story.season['action1']
        s2 = self.story.setting_sAB[season]['sA'].capitalize() + " and " + \
             self.story.setting_sAB[season]['sB'] + "."

        # s3 June and Charlie knew it was a day they would remember.
        s3 = self.protags + " knew it was a " + self.moment + " they would " + self.reaction + "."

        # s4A They would tell their children that the day they met 
        s4A = "They would tell their " + self.relations + " that the " + self.moment + " they " + self.action
        
        # s4B the air was sucked out of their lungs
        p1_phrase = self.story.theme['phrase']
        poss_p1_phrase = p1_phrase.replace('possessive', 'their')
        
        s4B = poss_p1_phrase
        
        # s4C they knew
        s4C = "they knew"
        
        s4 = s4A + " " + s4B + " and " + s4C + "."
        
        # s5 They just knew.
        s5 = "They just knew."


        p1 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5
        
        return p1

        
    def gen_action1(self):
                          
        action1 = self.gen_par1()

        return action1

    
    
    

