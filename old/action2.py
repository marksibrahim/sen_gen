"""
P4 - P6 
"""


class Action2():
    def __init__(self, our_story):
        self.story = our_story


    def narrator_in_setting(self):
        setting = "funeral"
        s1 =  self.story.narrator + " sat in the first row at "  + setting + "."
        s2 = self.story.characters[0][0]
        s2 += " was my best friend."
        s3 = " My feet stuck to the ground, not wanting to let go."
        return s1 + s2 + s3

    def dialogue(self):
        s1 = "\"I'm so sorry,\" I said."
        s2 = "Maybe " + self.story.theme + " is meant to be short."
        s3 = "I said those things, but " + self.story.narrator + " didn't know what I believed."
        return s1 + s2 + s3


    def draft(self):
        return self.narrator_in_setting() + self.dialogue()

