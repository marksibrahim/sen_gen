
# coding: utf-8

# In[ ]:

import random

class Action5():
    """
    generates Action 5, which is comprised of p17
    """

    def __init__(self, our_story):
        self.story = our_story

    def gen_par17(self):
    
        # s1 = < June > < got married > again < on a beach in Bermuda >.
        if self.story.season == "fall":
            location = "on an island off the coast of Maine"
        elif self.story.season == "winter":
            location = "on the tip of a mountain in Aspen"
        elif self.story.season == "spring":
            location = "in Amsterdam beside a canal"
        elif self.story.season == "summer":
            location = "on a beach in Bermuda"
        
        s1 = self.story.ch1['first_name'] + " " + self.story.action1_vb + " again " + location + "."
        
        # s2 = < The groom > had < a condo > there, < I > heard.
        if self.story.ch3['pronoun'] == "I":
            subject = "I"
        else:
            subject = self.story.ch3['first_name']
        
        s2 = self.story.action1_vb_addtl_ch.capitalize() + " had " + self.story.action1_vb_addtl_ch_possession +              " there, " + subject + " heard."
        
        # s3 = < I > < wasn't invited >.
        
        s3 = self.story.ch3['pronoun'].capitalize() + " " + self.story.action1_vb_entail_vb + "."
        
        # s4 = All < I > had was the < stone > < box > on < my > < bookshelf >.
        
        s4 = "All " + self.story.ch3['pronoun'] + " had was the " + self.story.symbol_adj +              " " + self.story.symbol_n + " on " + self.story.ch3['possessive'] + " " +              self.story.symbol_addtl_n + "."
        
        # s5 = Maybe < Charlie > was < lucky >, < I > thought.
        
        s5 = "Maybe " + self.story.ch2['first_name'] + " was " + self.story.surprise_opposite_adj +              ", " + self.story.ch3['pronoun'] + " thought."
        
        # s6 = Maybe < I > was < lucky > < to be alone > with the < box >.
        
        s6 = "Maybe " + self.story.ch3['pronoun'] + " was " + self.story.surprise_opposite_adj +              " " + self.story.protag_condition + " with the " + self.story.symbol_n + "."
        
        # s7 = < To be alone >.
        condition_capped = self.story.condition.capitalize()
        
        s7 = condition_capped + "."
        
        # s8 = But < I > couldn't convince < myself >.
        
        s8 = "But " + self.story.ch3['pronoun'] + " couldn't convince " +              self.story.ch3['reflexive_pn'] + "."

        p17 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7 + " " + s8
    
        
    def gen_action5(self):

        action5 = self.gen_par17()

        return action5

