
# coding: utf-8

# In[ ]:

import random


class Action6():
    """
    generates Action 6, which includes paragraphs 9-16, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story
        
        # par9 s1
        if self.story.ch3['pronoun'] == "I":
            self.pronoun = "We"
            self.s2_speaker = "I"
        else:
            self.pronoun = "They"
            self.s2_speaker = self.story.ch3['first_name']
            
        # p9 s1
        activity = ["met for coffee", "met for drinks"]
        self.chosen_activity = random.choice(activity)

        # p9 s2
        verb = ["arrived", "appeared", "showed up"]
        self.chosen_verb = random.choice(verb)        

        # p9 s2
        if self.story.season['action6'] == "fall":
            self.ch_state = "in a whirlwind of autumn leaves and red wool"
        elif self.story.season['action6'] == "winter":
            self.ch_state = "in a reckless flurry of snowflakes, wrapped in red wool"
        elif self.story.season['action6'] == "spring":
            self.ch_state = "with a sudden spring shower, shaking raindrops from a sleek black coat"
        elif self.story.season['action6'] == "summer":
            self.ch_state = "in a whirlwind of apology, cheeks flushed, arms lean and tan"

        # dialogue2 s2
        response1 = ["You knew. You knew.", "I don't understand.", "So then why--"]
        self.response1 = random.choice(response1)

        # dialogue2 s5B
        sipped = ["sipped from possessive cup", "sipped possessive drink"]
        sipped_choice = random.choice(sipped)
        self.poss_sipped_choice = sipped_choice.replace('possessive', self.story.ch1['possessive'])


    def gen_par9(self):
        
        # S1 = < We > < met for coffee > and < June > was late.
        s1A = self.pronoun + " " + self.chosen_activity
        s1B = self.story.ch1['first_name'] + " was late."
        s1 = s1A + " and " + s1B

        #S2 = < She > < arrived > < in a whirlwind of autumn leaves and red wool >.            
        s2 = self.story.ch1['pronoun'].capitalize() + " " + self.chosen_verb + " " + self.ch_state + "."

        p9 = s1 +  " " + s2
        
        return p9

    def gen_dialogue2(self):
        # dialogue1 is in Action4
        # This dialogue runs over p10-p15.
        
        # s1 = "I can't tell anyone else," < she > said. 
        #      "But I didn't < love > < Charlie >. Not after we < married >."            
        s1A = "\"I can't tell anyone else,\" " + self.story.ch1['pronoun'] + " said." 
        s1B = "\"But I didn't " + self.story.theme['verb'] + " " + self.story.ch2['first_name'] + "."
        s1C = "Not after we " + self.story.a1_surprise['action1_vb'] + ".\""
        s1 = s1A + " " + s1B + " " + s1C
        
        # s2 = "But the < summer > day," < I > said. " < You knew. You knew > ."
        s2A = "\"But the " + self.story.season['action1'] + " day,\" " + self.s2_speaker + " said."
        s2B = "\"" + self.response1 + "\""
        s2 = s2A + " " + s2B
        
        # s3 = "It was < the weather > , I think."
        s3 = "\"It was " + self.story.symbol['excuse'] + ", I think.\""
        
        # s4 = "No." < I > didn't mean for the word to come out. < My > throat was dry. 
        #      < I > tried to cough, but < the air was sucked out of my lungs >.
        p1_phrase = self.story.theme['phrase']
        poss_p1_phrase = p1_phrase.replace('possessive', self.story.ch3['possessive'])
        
        s4A = "\"No.\"" + " " + self.story.ch3['pronoun'].capitalize() + \
              " didn't mean for the word to come out."
        s4B = self.story.ch3['possessive'].capitalize() + " throat was dry."
        s4C = self.story.ch3['pronoun'].capitalize() + " tried to cough, but " + poss_p1_phrase + "."        
        s4 = s4A + " " + s4B + " " + s4C
        
        # s5 = "I don't know." < She > < sipped from her cup >. "I'm too < romantic >. 
        #       In love with < love >. In love with something else maybe." < She > shrugged. 
        #      "Who knows? Am I a terrible person?"
        s5A = "\"I don't know.\""
        s5B = self.story.ch1['pronoun'].capitalize() + " " + self.poss_sipped_choice + "."
        s5C = "\"I'm too " + self.story.theme['adj'] + ". In love with " +  self.story.theme['noun'] + \
              ". In love with something else maybe.\""
        s5D = self.story.ch1['pronoun'].capitalize() + " shrugged."
        s5E = "\"Who knows? Am I a terrible person?\""
        
        s5 = s5A + " " + s5B + " " + s5C + " " + s5D + " " + s5E
        
        # s6 = "No," < I > said.
        s6 = "No,\"" + " " + self.story.ch3['pronoun'] + " said."

        dialogue2 = s1 + '\n\n' + s2 + '\n\n' + s3 + '\n\n' + s4 + '\n\n' + s5 + '\n\n' + s6
        
        return dialogue2
   

    def gen_par16(self):
                  
        # s1s2 = But < I > didn't say it. The word got caught in < my > throat.                  
        s1s2 = "But " + self.story.ch3['pronoun'] + " didn't say it. The word got caught in " + \
                self.story.ch3['possessive'] + " throat."
        
        # s3 = < I > could feel the weight of the < stone > < box > in < my > hand.
        s3 = self.story.ch3['pronoun'].capitalize() + " could feel the weight of the " + \
             self.story.symbol['adj'] + " " + self.story.symbol['noun'] + " in " + \
             self.story.ch3['possessive'] + " hand."
        
        # s4 = < I > clenched < my > fist.
        s4 = self.story.ch3['pronoun'].capitalize() + " clenched " + self.story.ch3['possessive'] + " fist."
        
        p16 = s1s2 + " " + s3 + " " + s4
                  
        return p16

        
    def gen_action6(self):
                  
        par9 = self.gen_par9()
        dialogue2 = self.gen_dialogue2()
        par16 = self.gen_par16()
        action6 = par9 + '\n\n' + dialogue2 + '\n\n' + par16

        return action6
    

