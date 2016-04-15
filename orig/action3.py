
# coding: utf-8

# In[ ]:

import random

class Action3():
    """
    generates Action 3 -- the inciting event or surprise -- which is comprised of 
    paragraph 3, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story

        season = self.story.season['action3']
        if season == "fall":
            self.s2 = self.story.setting_sAB[season]['sC'].capitalize()
        else:
            self.s2 = self.story.setting_sAB[season]['sB'].capitalize()

        phrase = ['The weather shifted and shifted', 
                  'The year rolled through the seasons', 
                  'Time passed, the weather shifted', 
                  'The year crept by', 
                  'Season after season, the year slid in its circle']
        self.phrase = random.choice(phrase)

        if season == 'spring':
            sports = ['running', 'bird watching', 'mushroom hunting']
        elif season == 'summer':
            sports = ['biking', 'kayaking', 'golfing']
        elif season == 'fall':
            sports = ['rock climbing', 'fishing', 'playing tennis']
        elif season == 'winter':
            sports = ['snowshoeing', 'skiing', 'snow boarding']
        self.sports_verb = random.choice(sports)

        unexpected = ['unexpected', 'swift and astonishing', 'sudden']
        self.unexpected = random.choice(unexpected)
        
        if self.story.ch3['pronoun'] == "I":
            self.pronoun = "I"
        else:
            self.pronoun = self.story.ch3['first_name']

        
    def gen_par1(self):
        
        # s1 = The weather shifted and shifted until it was another summer day.    
        s1 = self.phrase + " until it was another " + self.story.season['action3'] + " day."

        # s2 = The air was so heavy it was hard to breath.
        s2 = self.s2 + "."

        # s3 = < Charlie > was < golfing >.
        s3 = self.story.ch2['first_name'] + " was " + self.sports_verb + "."

        # s4 = That's what June told me.
        s4 = "That's what " + self.story.ch1['first_name'] + " told " + self.story.ch3['object_pn'] + "."

        # s5 = But the storm was so < unexpected >, there was no reason to believe it would come
        s5 = "The storm was so " + self.unexpected + "," + " there was no reason to believe it would come."

        # s6 = When the lightning struck, it stopped < his > heart.        
        s6 = "When the lightning struck, it stopped " + self.story.ch2['possessive'] + " heart."

        # s7 = < His > hair was burned to the scalp, < his > skin tattooed with fractals 
        #      as < his > capillaries burst.
        s7 = self.story.ch2['possessive'].capitalize() + " hair was burned to the scalp, " + \
             self.story.ch2['possessive'] + " skin tattooed with fractals as " + \
             self.story.ch2['possessive'] + " capillaries burst."

        # s8 = That was more than < I > wanted to know.
        s8 = "That was more than " + self.pronoun + " wanted to know."

        p1 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7 + " " + s8

        return p1

    
    def gen_action3(self):

        action3 = self.gen_par1()

        return action3


# In[ ]:



