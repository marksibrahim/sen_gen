"""
authors a short story based on a theme
"""


import random

class Story():
    """
    theme
        contains opening, conflict, resolution
    characters
        name + gender, units: family
    setting
    """

    def __init__(self, noun_prompt):
        """
        global variables for our story
        """
        self.noun_prompt = noun_prompt

        self.characters = {}
        self.theme =  "love"

    def gen_character(self, gender):
        """
        returns a character name based given gender
        TODO: Keri to fill in functionality
        """
        name = "Tom"
        return name


if __name__ == "__main__":
    our_story = Story()

    print(" ")
    
