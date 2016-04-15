import random

class Action2():
    """
    generates Action 2, which is comprised of paragraph 2, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story

        if self.story.season['action2'] == "winter":
            setting = ["in a hilltop chapel", 
                            "in a repurposed factory in SoDo", 
                            "at ranch in Napa Valley", 
                            "at someone's parent's enormous house in the suburbs"
                           ]
        else:
            setting = ["under St. John's Bridge", 
                            "in a repurposed factory in SoDo", 
                            "on a wide green lawn", 
                            "in a hilltop chapel", 
                            "at someone's parent's enormous house in the suburbs"]
        self.setting = random.choice(setting)
        

        if self.story.ch3['pronoun'] == "I":
            self.subject = "I"
            self.possessive = "My"
        else:
            self.subject = self.story.ch3['first_name']
            self.possessive = self.story.ch3['first_name'] + "'s"
            

        s11_phrase = ["life seemed so", "life was so", "life always felt"]
        self.s11_phrase = random.choice(s11_phrase)
            

        if self.story.story_type == "1":
            self.weather_adj1 = "dry"
            self.weather_adj2 = "cold"

            self.body_part1 = "hair"
            self.body_part2 = "hands were"
            self.body_part_adj = "dry"
            self.body_part_v1 = "stuck out"
            self.body_part_v2 = "cry"
            self.body_part_phrase = "it wouldn't lay down for"

            self.metaphor1 = "was floating out from"
            self.metaphor2 = "head as though a magnet were pulling the ends away from"
            self.reaction = "smoothed it down"

            self.action1 = "they kissed"
            self.action2 = "the audience applauded"

        else:
            self.weather_adj1 = "heavy"
            self.weather_adj2 = "cold"

            self.body_part1 = "phone"
            self.body_part2 = "hands were"
            self.body_part_adj = "sweaty"
            self.body_part_v1 = "felt like a brick that wanted to build something or smash it,"
            self.body_part_v2 = "let them know"
            self.body_part_phrase = "it didn't say what they thought about"

            self.metaphor1 = "was cramping"
            self.metaphor2 = "hand and it was either excitement or hostility that overwhelmed"
            self.reaction = "put it down"

            self.action1 = "they kissed"
            self.action2 = "the phone went dead"


    def gen_par1(self):
        
        # s1 = They < got married >  < on a wide green lawn > and < I > < was sitting > 
        #      < in the first row >.
        s1 = "They " + self.story.a1_surprise['action1_vb'] + " " + self.setting + " and " + \
             self.story.ch3['pronoun'] + " " + self.story.event['relationship']['event1_v'] + \
             " " + self.story.event['relationship']['location'] + "."
        
        # s2 = The air was < dry > that day and it was < cold >.
        s2 = "The air was " + self.weather_adj1 + " that day and it was " + self.weather_adj2 + "."
        
        # s3 = < My > < hair > < was floating out from > < my > < head as though a magnet were pulling 
        #      the ends away from > < me >.
        s3 = self.possessive + " " + self.body_part1 + " " + \
             self.metaphor1 + " " + self.story.ch3['possessive'] + " " + self.metaphor2 + " " + \
             self.story.ch3['object_pn'] + "."
        
        # s4 = < I > < smoothed it down > as < they kissed > and < the audience applauded >.
        s4 = self.story.ch3['pronoun'].capitalize() + " " + self.reaction + " as " + self.action1 + \
             " and " + self.action2 + "."
        
        # s5 = < My > < hands were > < dry > and < I > tried.
        s5 = self.story.ch3['possessive'].capitalize() + " " + self.body_part2 + " " + self.body_part_adj + \
             " and " + self.story.ch3['pronoun'] + " tried."
        
        # s6 = < I > tried, but it was < hopeless >.
        s6 = self.story.ch3['pronoun'].capitalize() + " tried, but it was " + \
             self.story.theme['action1_adj'] + "."
        
        # s7 = < My > < hair > < stuck out > and < I > wanted to < cry > that 
        #      < it wouldn't lay down for > me.
        s7 = self.story.ch3['possessive'].capitalize() + " " + self.body_part1 + " " + \
             self.body_part_v1 + " and " + self.story.ch3['pronoun'] + " wanted to " + \
             self.body_part_v2 + " that " + self.body_part_phrase + " " + self.story.ch3['object_pn'] + "."
        
        
        if self.story.noun_prompt_obj.abstraction:
            abstract_article = ""
        else:
            abstract_article = "the "
            
        first_letter = self.story.noun_prompt_obj.noun[:1]
        
        if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
            second_article = "an "
        elif self.story.noun_prompt_obj.abstraction:
            second_article = ""
        else:
            second_article = "a "

            
        s8 = "That was when " + self.story.ch3['pronoun'] + " started having the dreams about "  + abstract_article + self.story.noun_prompt + "."

        s9 = "A man would say, \"" + self.story.gen_sentences.generate_sents_w_noun(self.story.noun_prompt_obj.noun)[0] + ".\""
        
        s10 = " And I would reply, \"" + self.story.gen_sentences.generate_sents_w_noun(self.story.noun_prompt_obj.noun)[0]  
        s10 += ".\" It was unsettling. Why was I dreaming about " + second_article + self.story.noun_prompt_obj.noun + "?"
        
        s11 = self.subject + " thought it was because " + self.story.ch3['possessive'] + " " + \
              self.s11_phrase + " just outside of " + self.story.ch3['possessive'] + " reach."  
            
        s12 = "And then one day, the dreams stopped."

        
        p1 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7 + "\n\n" + \
             s8 + " " + s9 + " " + s10 + " " + s11 + " " + s12
        
        return p1


    def gen_action2(self):
                  
        action2 = self.gen_par1()

        return action2
    

