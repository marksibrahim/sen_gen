"""
generates first paragraph based on elements in story.py
"""

import random

#create story instance to use in generation of first paragraph


class Par2():
    """
    drafts second paragraph based on elemnts in 
    instance of story provided
    """
    def __init__(self, our_story):
        self.story = our_story

    def gen_marriage(self):
        setting = ['in a church', 'on a green lawn', 'on a hill top']
        marriage_syn = ['got hitched', 'got married', 'said their vows ']
        s1 = "They " + random.choice(marriage_syn) + " " + random.choice(setting)
        s1 += " and I was sitting in the front row. "
        return s1

    def describe_narrator(self):
        s2 = "My hair was floating as if "
        floating_metaphors = ["carried by a river", "a magnet were pulling the ends"]
        s2 += random.choice(floating_metaphors) + ". "
        s3 = "I smoothed it out as they kissed. "
        s4 = "I wanted to " + random.choice(["yell out", "scream"])
        s4 += "go down."
        return s2 + s3 + s4 

    def draft_par(self):
        return  self.gen_marriage() + self.describe_narrator()

