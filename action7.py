import random

class Action7():
    """
    generates Action 7, which is comprised of p17
    """

    def __init__(self, our_story):
        self.story = our_story

        # p17 s1
        if self.story.season['action7'] == "fall":
            self.location = "on an island off the coast of Maine"
        elif self.story.season['action7'] == "winter":
            self.location = "on the tip of a mountain in Aspen"
        elif self.story.season['action7'] == "spring":
            self.location = "in Amsterdam beside a canal"
        elif self.story.season['action7'] == "summer":
            self.location = "on a beach in Bermuda"

        # p17 s2
        if self.story.ch3['pronoun'] == "I":
            self.subject = "I"
        else:
            self.subject = self.story.ch3['first_name']
            
        addtl_ch = self.story.a1_surprise['action1_vb_addtl_ch']

        if self.story.ch2['gender'] == "female" and addtl_ch == "the groom":
            self.addtl_ch = "The bride"
        else:
            self.addtl_ch = "The groom"
        

        
    def gen_par1(self):
    
        # s1 = < June > < got married > again < on a beach in Bermuda >.
        s1 = self.story.ch1['first_name'] + " " + self.story.a1_surprise['action1_vb'] + \
             " again " + self.location + "."
        
        # s2 = < The groom > had < a condo > there, < I > heard.        
        s2 = self.addtl_ch + " had " + self.story.a1_surprise['action1_vb_addtl_ch_possession'] + \
             " there, " + self.subject + " heard."
        
        # s3 = < I > < wasn't invited >.        
        s3 = self.story.ch3['pronoun'].capitalize() + " " + self.story.a1_surprise['action1_vb_entail_vb'] + "."
        
        # s4 = All < I > had was the < stone > < box > on < my > < bookshelf >.
        s4 = "All " + self.story.ch3['pronoun'] + " had was the " + self.story.symbol['adj'] + " " + \
             self.story.symbol['noun'] + " on " + self.story.ch3['possessive'] + " " + self.story.symbol['assoc_noun'] + "."
        
        # s5 = Maybe < Charlie > was < lucky >, < I > thought.
        s5 = "Maybe " + self.story.ch2['first_name'] + " was " + \
             self.story.a1_surprise['surprise_opposite_adj'] + ", " + self.story.ch3['first_name'] + " thought."
        
        # s6 = Maybe < I > was < lucky > < to be alone > with the < box >.
        s6 = "Maybe " + self.story.ch3['pronoun'] + " was " + self.story.a1_surprise['surprise_opposite_adj'] + \
             " " + self.story.theme['protag_condition'] + " with the " + self.story.symbol['noun'] + "."
        
        # s7 = < To be alone >.
        condition_capped = self.story.theme['protag_condition'].capitalize()        
        s7 = condition_capped + "."
        
        # s8 = But < I > couldn't convince < myself >.
        s8 = "But " + self.story.ch3['pronoun'] + " couldn't convince " + self.story.ch3['reflexive_pn'] + "."

        p17 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7 + " " + s8
        
        return p17
    
        
    def gen_action7(self):

        action7 = self.gen_par1()

        return action7
