
# coding: utf-8

# In[ ]:

import random


class Action5():
    """
    generates Action 5, which is comprised of paragraph 8, based on elements in py
    """
    
    def __init__(self, our_story):
        self.story = our_story

        protag_situation = "possessive skin was sweaty and hot"
        self.protag_situation = protag_situation.replace('possessive', self.story.ch3['possessive'])
        
        if self.story.ch3['pronoun'] == "I":
            self.repeat_action = "went to work and came home, went to work and came home"
            self.object_pn = self.story.ch4['object_pn']
            self.s8_subject = self.story.ch3['pronoun']
        else:
            self.repeat_action = "went to work and went home in a misleadingly smooth cycle"
            self.object_pn = self.story.ch4['first_name']
            self.s8_subject = self.story.ch3['first_name']
            
        op2 = self.story.ch3['pronoun'] + " couldn't shake the feeling that"
        op3 = "somehow " + self.story.ch3['pronoun'] + " knew that" 
            
        s11_options = ["they always felt as though", op2, op3]    
        self.s11_options = random.choice(s11_options)
        
        s12_options = ["tried not to think about them", "cleaned the house and found some money in a pocket"]
        self.s12_options = random.choice(s12_options)
        
            
    def gen_par1(self):
        
        # s1 = < I > put < my > < box > on the < bookcase> .
        s1 = self.story.ch3['pronoun'].capitalize() + " put " + self.story.ch3['possessive'] + \
             " " + self.story.symbol['noun'] + " on the " + self.story.symbol['assoc_noun'] + "."
        
        # s2 = It was < cool >, always < cool> , even when < my > skin was sweaty and hot >.
        s2 = "It was " + self.story.symbol['adj_temp'] + ", always " + self.story.symbol['adj_temp'] + \
             ", even when " + self.protag_situation + "."
        
        # s3 = < Ethan > and < I > tried.
        if self.story.ch3['pronoun'] == "I":
            s3 = self.story.ch4['first_name'] + " and " + self.story.ch3['pronoun'] + " tried."
        else:
            s3 = self.story.ch4['first_name'] + " and " + self.story.ch3['first_name'] + " tried."
        
        # s4 = < I > < thought we did. >
        if self.story.ch3['pronoun'] == "I":
            s4 = self.story.ch3['pronoun'] + " thought we did."
        else:
            s4 = self.story.ch3['pronoun'].capitalize() + " thought they did."
        
        # s5 = < Ethan > from the < funeral >, from the < wedding >, too, 
        #      though < I > hadn't noticed < him > then.
        event = self.story.event['relationship']['event2']
        event_word = event.split()
        
        s5 = self.story.ch4['first_name'] + " from the " + event_word[2] + ", from the " + \
             self.story.event['relationship']['event1'] + ", too, though " + self.s8_subject + \
             " hadn't noticed " + self.story.ch4['object_pn'] + " then."
        
        # s6 = He came by almost every day, then not at all.
        s6 = self.story.ch4['pronoun'].capitalize() + " came by almost every day, then not at all."
        
        # s7 = It was confusing and sad.
        s7 = "It was confusing and sad."
        
        # s8 = I went to work and came home, went to work and came home, touched the box with my fingertips.
        s8 = self.s8_subject + " " + self.repeat_action + ", touched the " + \
             self.story.symbol['noun'] + " with " + self.story.ch3['possessive'] + " fingertips."
            
            
        # s9 =  I started having the dreams again. They were even stranger. 
        s9 = self.story.ch3['pronoun'].capitalize() + " started having the dreams again." + \
             " " + "They were even stranger."
        
        # s10 = Markov sentence. Markov sentence. 
        s10 = "Markov sentence. Markov sentence."
        
        # s11 = Yet somehow < list options > they pointed to the < box >.
        s11 = "Yet " + self.s11_options + " they pointed to the " + self.story.symbol['noun'] + "."
        
        
        # s12 = < I > < options > Then < June > called to get together.     
        s12 = self.s8_subject + " " + self.s12_options + ". Then " + self.story.ch1['first_name'] + \
              " called to get together."
        
              
        p1 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7 + " " + s8 + "\n\n" + \
             s9 + " " + s10 + " " + s11 + " " + s12
        
        return p1


    def gen_action5(self):
                  
        action5 = self.gen_par1()

        return action5
    

