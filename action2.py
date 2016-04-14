import random

class Action2():
    """
    generates Action 2, which is comprised of paragraph 2, based on elements in story.py
    """
    
    def __init__(self, our_story):
        self.story = our_story

        if self.story.season['winter'] == "winter":
            self.setting = ["in a hilltop chapel", 
                            "in a repurposed factory in SoDo", 
                            "at ranch in Napa Valley", 
                            "at someone's parent's enormous house in the suburbs"
                           ]
        else:
            self.setting = ["under St. John's Bridge", 
                            "in a repurposed factory in SoDo", 
                            "on a wide green lawn", 
                            "in a hilltop chapel", 
                            "at someone's parent's enormous house in the suburbs"]
        
        self.weather_adj1 = "dry"
        self.weather_adj2 = "cold"
        
        self.body_part1 = "hair"
        self.body_part2 = "hands were"
        self.body_part_adj = "dry"
        self.body_part_v1 = "stuck out"
        self.body_part_v2 = "cry"
        self.body_part_phrase = "it wouldn't lay down for me"
        
        self.metaphor1 = "was floating out from"
        self.metaphor2 = "head as though a magnet were pulling the ends away from"
        self.reaction = "smoothed it down"
        
        self.action1 = "they kissed"
        self.action2 = "the audience applauded"


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
        s3 = self.story.ch3['possessive'].capitalize() + " " + self.body_part1 + " " + \
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
        #      < it wouldn't lay down for me >.
        s7 = self.story.ch3['possessive'].capitalize() + " " + self.body_part1 + " " + \
             self.body_part_v1 + " and " + self.story.ch3['pronoun'] + " wanted to " + \
             self.body_part_v2 + " that " + self.body_part_phrase + "."

        
        p1 = s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 + " " + s6 + " " + s7
        
        return p1


    def gen_action2(self):
                  
        action2 = self.gen_par1()

        return action2
    

