
# coding: utf-8

# In[ ]:

import random

class Action6():
    """
    generates Action 6, which includes paragraphs 18-21, based on elements in story.py
    """

    def __init__(self, our_story):
        self.story = our_story

    def gen_par18(self):
        
        # s1 = The snow was piling up and it was cold, getting colder.
        if self.story.season == "winter":
            s1 ="The snow was piling up and it was cold, getting colder."
        elif self.story.season == "spring":
            s1 ="Buds were poking up from the earth, the winter chill fading."
        elif self.story.season == "summer":
            s1 ="It was green and green everywhere, bursting from every nook and cranny, the air hanging hot and still."
        elif self.story.season == "fall":
            s1 ="The leaves were falling off the trees, the sun arcing lower across the sky."
            
        # s2 & s3 = < I > < emailed > < June >.  < I > < texted > < her >.
        
        s2 = self.story.ch3['pronoun'] + " " + self.story.contact_v1 + " " + self.story.ch1['first_name'] + "."
        s3 = self.story.ch3['pronoun'] + " " + self.story.contact_v2 + " " + self.story.ch1['object_pn'] + "."
        
        # s4 = Finally I saw her at a restaurant and waited until she was leaving.

        s4 = "Finally " + self.story.ch3['pronoun'] + " saw " + self.story.ch1['object_pn'] +              " at a " + self.story.place + " and waited until " + self.story.ch1['pronoun'] + " was leaving." 
        
        
        p18 = s1 + " " + s2 + " " + s3 + " " + s4
        
        return p18


    def gen_dialogue3(self):
        
        # This dialogue is p19 - p21.
        
        # p19 -- "I'm sorry," < I > said.  "I didn't know."  
        s1A = "\"I'm sorry,\" " + self.story.ch3['pronoun'] + " said."
        s1B = "\"I didn't know.\""
        s1 = s1A + " " + s1B
        
        # p19 -- < She > turned to leave.
        s2 = self.story.ch1['pronoun'].capitalize() + " turned to leave."
        
        # p19 -- "I don't know how < love > can < die > so easily. Can it really?"
        s3 = "\"I don't know how " +  self.story.theme_n + " can " + self.story.surprise_v +              " so easily. Can it really?\""
        
        p19 = s1 + " " + s2 + " " + s3
        
        # p20 -- She put a hand on my arm.
        s4 = self.story.ch1['pronoun'].capitalize() + " put a hand on " +              self.story.ch3['possessive'] + " arm."
        
        # p20 -- Her mouth opened and I thought she would say, "Yes."  Or maybe "No."
        s5 = self.story.ch1['possessive'].capitalize() + " mouth opened and " +              self.story.ch3['pronoun'] + " thought " + self.story.ch1['pronoun'] +              " would say, \"Yes.\"  Or maybe \"No.\""
        
        # p20 -- It didn't matter which one.        
        s6 = "It didn't matter which one."
        
        p20 = s4 + " " + s5 + " " + s6 
        
        # p21 -- "Is it so fragile?" I said as she shook her head and left.   
        s7 = "\"Is it so " + self.story.theme_adj_question + "?\" " + self.story.ch3['pronoun'] +              " said as " + self.story.ch1['pronoun'] + " shook " + self.story.ch1['possessive'] + " head and left."
        
        p21 = s7

        dialogue3 = p19 + '\n' + p20 + '\n' + p21
        
        return dialogue3


    def gen_action6(self):
                  
        par18 = self.gen_par18()
        dialogue3 = self.gen_dialogue3()
        action6 = par18 + '\n' + dialogue3

        return action6
    

