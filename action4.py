
# coding: utf-8

# In[ ]:

import random

class Action4():
    """
    generates Action 4, which includes paragraphs 9-16, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story

    def gen_par9(self):
        
        # S1 = < We > < met for coffee > and < June > was late.
        
        # set pronoun
        if self.story.ch3['pronoun'] == "I":
            pronoun = "We"
        else:
            pronoun = "They"
        
        activity = ["met for coffee", "met for drinks"]
        chosen_activity = random.choice(activity)
        
        s1A = pronoun + " " + chosen_activity
        s1B = self.story.ch1['first_name'] + " was late."
        s1 = s1A + " and " + s1B

        #S2 = < She > < arrived > < in a whirlwind of autumn leaves and red wool >.
        
        verb = ["arrived", "appeared", "showed up"]
        chosen_verb = random.choice(verb)        
        
        if self.story.season == "fall":
            ch_state = "in a whirlwind of autumn leaves and red wool"
        elif self.story.season == "winter":
            ch_state = "in a reckless flurry of snowflakes, wrapped in red wool"
        elif self.story.season == "spring":
            ch_state = "with a sudden spring shower, shaking raindrops from her coat"
        elif self.story.season == "summer":
            ch_state = "in a whirlwind of apology, cheeks flushed, arms lean and tan"
            
        s2 = self.story.ch1['pronoun'].capitalize() + " " + chosen_verb + " " + ch_state + "."

        p9 = s1 +  " " + s2
        
        return p9

    def gen_dialogue2(self):
        
        # This dialogue runs over p10-p15.
        
        # s1 = "I can't tell anyone else," < she > said. 
        #      "But I didn't < love > < Charlie >. Not after we < married >."
            
        s1A = "\"I can't tell anyone else,\"" + self.story.ch1['pronoun'] + " said." 
        s1B = "\"But I didn't " + self.story.theme_v + " " + self.story.ch2['first_name'] + "."
        s1C = "Not after we " + action1_vb + ".\""
        s1 = s1A + " " + s1B + " " + s1C
        
        # s2 = "But the < summer > day," < I > said. " < You knew. You knew > ."
    
        response1 = ["You knew. You knew.", "I don't understand.", "So then why--"]
        response1 = random.choice(response1)
        s2A = "\"But the " + self.story.season + " day,\" " + self.story.ch3['pronoun'] + " said."
        s2B = "\"" + response1 + "\""
        s2 = s2A + " " + s2B
        
        # s3 = "It was < the weather > , I think."
        
        s3 = "\"It was " + excuse_n + ", I think.\""
        
        # s4 = "No." < I > didn't mean for the word to come out. < My > throat was dry. 
        #      < I > tried to cough, but < the air was sucked out of my lungs >.

        p1_phrase = "the air was sucked out of possessive lungs"
        new_p1_phrase = p1_phrase.replace('possessive', self.story.ch3['possessive'])
        
        s4A = "\"No.\"" + " " + self.story.ch3['pronoun'].capitalize() +               " didn't mean for the word to come out."
        s4B = self.story.ch3['possessive'].capitalize() + " throat was dry."
        s4C = self.story.ch3['pronoun'].capitalize() + " tried to cough, but " +               new_p1_phrase + "."        
        s4 = s4A + " " + s4B + " " + s4C
        
        # s5 = "I don't know." < She > < sipped from her cup >. "I'm too < romantic >. 
        #       In love with < love >. In love with something else maybe." < She > shrugged. 
        #      "Who knows? Am I a terrible person?"

        sipped = ["sipped from possessive cup", "sipped possessive drink"]
        sipped_choice = random.choice(sipped)
        new_sipped_choice = sipped_choice.replace('possessive', self.story.ch1['possessive'])

        s5A = "\"I don't know.\""
        s5B = self.story.ch1['pronoun'].capitalize() + " " + new_sipped_choice + "."
        s5C = "\"I'm too " + self.story.theme_adj + ". In love with " +  self.story.theme_n +               ". In love with something else maybe.\""
        s5D = self.story.ch1['pronoun'].capitalize() + " shrugged."
        s5E = "\"Who knows? Am I a terrible person?\""
        
        s5 = s5A + " " + s5B + " " + s5C + " " + s5D + " " + s5E
        
        # s6 = "No," < I > said.
        s6 = "No,\"" + " " + self.story.ch3['pronoun'] + " said."

        dialogue2 = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6
        
        return dialogue2
   

    def gen_par16(self):
                  
        # s1s2 = But < I > didn't say it. The word got caught in < my > throat.
                  
        s1s2 = "But " + self.story.ch3['pronoun'] + " didn't say it. The word got caught in " +                self.story.ch3['possessive'] + " throat."
        
        # s3 = < I > could feel the weight of the < stone > < box > in < my > hand.
                  
        s3 = self.story.ch3['pronoun'].capitalize() + " could feel the weight of the " + self.story.symbol_adj +              " " + self.story.symbol_n + " in " + self.story.ch3['possessive'] + " hand."
        
        # s4 = < I > clenched < my > fist.
        
        s4 = self.story.ch3['pronoun'].capitalize() + " clenched " + self.story.ch3['possessive'] + " fist."
        
        p16 = s1s2 + " " + s3 + " " + s4
                  
        return p16

        
    def gen_action4(self):
                  
        par9 = self.gen_par9()
        dialogue2 = self.gen_dialogue2()
        par16 = self.gen_par16()
        action4 = par9 + '\n' + dialogue2 + '\n' + par16

        return action4
    

