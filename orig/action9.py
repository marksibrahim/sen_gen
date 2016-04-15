import random

class Action9():
    """
    generates Action 9 -- the resolution -- which is comprised of paragraph 22, 
    based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story
        
        if self.story.ch3['pronoun'] == "I":
            self.verb1 = "know"
            self.verb2 = "hold"
            self.verb3 = "feel"
        else:
            self.verb1 = "knows"
            self.verb2 = "holds"
            self.verb3 = "feels"

    def gen_par22(self):
        
        # But < I > knew it couldn't be. < I > < know > it can't be.
        s1 = "But " + self.story.ch3['pronoun'] + " knew it couldn't be. " + \
              self.story.ch3['pronoun'].capitalize() + " " + self.verb1 + " it can't be."
        
        # The < stone > < box > sits on < my > < bookshelf > and is always < cool >.
        s2 = "The " + self.story.symbol['adj'] + " " + self.story.symbol['noun'] + \
             " sits on " + self.story.ch3['possessive'] + " " + self.story.symbol['assoc_noun'] + \
             " and is always " + self.story.symbol['adj_temp'] + "."
        
        # It's < heavy > and < light > at the same time.          
        s3 = "It's " + self.story.symbol['adj_weight'] + " and " + \
             self.story.symbol['adj_weight_opposite2'] + " at the same time."
        
        # When < I > hold it, < I > feel < hopeful > .
        s4 = "When " + self.story.ch3['pronoun'] + " " + self.verb2 + " it, " + self.story.ch3['pronoun'] + \
             " " + self.verb3 + " " + self.story.theme['resolution_adj'] + "."
        
        p22 = s1 + " " + s2 + " " + s3 + " " + s4
        
        return p22
    
    def gen_action9(self):
                  
        action9 = self.gen_par22()

        return action9

