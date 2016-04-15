
# coding: utf-8

# In[ ]:

import random

class Action4():
    """
    generates Action 4, which includes paragraphs 4, 5, 6 and 7 (renamed to 
    "par1", "dialogue1," etc., here), based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story

        if self.story.ch1['gender'] == 'male':
            relationship = ["best friend", "brother", "cousin", "business partner"]
        else:
            relationship = ["best friend", "sister", "cousin", "business partner"]
        self.relation = random.choice(relationship)

        if self.story.season['action4'] == "winter":
            self.ground_state1 = "the ground felt soft"
            self.weather_verb = "snowing"
            self.feet = "boots sunk"
            self.ground_state2 = "snow"
            self.ground_state3 = "the ground was hard"
        else:
            self.ground_state1 = "the ground was soft"
            self.weather_verb = "raining"
            self.feet = "heels sucked "
            self.ground_state2 = "mud"
            self.ground_state3 = "the ground was soft"
            
        d_line1 = ["I'm so sorry", "How could this happen", "I don't understand"]
        self.dialogue_line1 = random.choice(d_line1)
        
        action = "placed a hand on possessive arm"
        self.poss_action = action.replace('possessive', self.story.ch1['possessive'])
        
        self.gift_recipients = "us each"
        self.gift_how = "in our hands"

        if self.story.ch3['pronoun'] == "I":
            self.pronoun = "I"
        else:
            self.pronoun = self.story.ch3['first_name']
            
        if self.story.ch3['pronoun'] == "I":
            self.possessive = "my"
        else:
            self.possessive = self.story.ch3['first_name'] + "'s"
            

    def gen_par1(self):
        
        # < I > < sat > < in the first row > < at the funeral >.
        s1 = self.pronoun + " " + self.story.event['relationship']['event2_v'] + \
             " " + self.story.event['relationship']['location'] + " " + \
             self.story.event['relationship']['event2'] + "."

        # < June > was < my > < best friend >.
        s2 = self.story.ch1['first_name'] + " was " + self.story.ch3['possessive'] + \
             " " + self.relation

        if self.relation == 'business partner' and self.story.ch1['gender'] == 'male':
            s2 = s2 + ", but he was more than that."
        elif self.relation == 'business partner' and self.story.ch1['gender'] == 'female':  
            s2 = s2 + ", but she was more than that."
        else:
            s2 = s2 + "."

        # < The ground was soft > because it had been < raining >.
        s3 = self.ground_state1.capitalize() + " because it had been " + self.weather_verb + "."

        # < My > < heels sucked > into the < mud >, not wanting to let go.
        s4 = self.story.ch3['possessive'].capitalize() + " " + self.feet + " into the " + \
             self.ground_state2 + ", not wanting to let go."

        p1 = s1 + " " + s2 + " " + s3 + " " + s4
            
        return p1

    
    def gen_dialogue1(self):
        # dialogue2 is in Action6
        # this is essentially par2

        # "< I'm so sorry >," < I > said.
        line1 = "\"" + self.dialogue_line1 + ",\" " + self.story.ch3['pronoun'] + " said."
        
        # "Maybe you and < Charlie > were too < lucky >. Maybe < love > is only meant to be < short >."
        line2 = "\"Maybe you and " + self.story.ch2['first_name'] + " were too " + \
                self.story.a1_surprise['surprise_opposite_adj'] + ". Maybe " + \
                self.story.theme['noun'] + " is only meant to be " + self.story.theme['n_adj'] + \
                ".\""
        
        # < I > said those things but < I > didn't know what < I > believed.
        line3 = self.story.ch3['pronoun'].capitalize() + " said those things but " + \
                self.story.ch3['pronoun'] + " didn't know what " + self.story.ch3['pronoun'] + \
                " believed."
                
        dialogue1 = line1 + " " + line2 + " " + line3

        return dialogue1
    

    def gen_pars3_4(self):

        # < She > shook < her > head and < placed a hand on > < her > arm.
        s1 = self.story.ch1['first_name'].capitalize() + " shook " + self.story.ch1['possessive'] + \
             " head and placed a hand on " + self.possessive + " arm."
        
        # < The ground was soft > < but > < he > < wasn't > < buried >.
        if self.story.season['action4'] == "winter":
            s2 = self.story.ch2['first_name'] + " wasn't " + \
                 self.story.event['relationship']['event2_v2'] + "."
        else:
            s2 = self.ground_state1.capitalize() + " but " + self.story.ch2['first_name'] + \
                 " wasn't " + self.story.event['relationship']['event2_v2'] + "."
        
        # < June > gave < us each > a small box of stone, hollow in the center, 
        # his ashes heavy and weightless in our hands.
        s3 = self.story.ch1['first_name'] + " gave " + self.gift_recipients + " a " + \
             self.story.symbol['adj_aux'] + " " + self.story.symbol['noun'] + " of " + \
             self.story.symbol['adj'] + ", " + self.story.symbol['adj_prop'] + ", " + \
            self.story.ch2['first_name'] + "'s " + self.story.event['relationship']['noun'] + \
             " " + self.story.symbol['adj_weight'] + " and " + self.story.symbol['adj_weight_opposite1'] + \
             " " + self.gift_how + "."
        
        p3p4 = s1 + " " + s2 + " " + s3

        return p3p4
    
    def gen_action4(self):

        action4 = self.gen_par1() + '\n\n' + self.gen_dialogue1() + '\n\n' + self.gen_pars3_4()

        return action4

