"""
generate first paragraph of a story 
based on microdoc
"""

import random

seasons = ['hot summer', 'cold winter', 'rainy spring', 'crisp fall']
characters_1 = ['June', 'Evelyn', 'Mary', 'Roselyn']
characters_2 = ['Charlie', 'Tom', 'Holden']

character1 = random.choice(characters_1)
character2 = random.choice(characters_2)


class First_Par():
    """
    generates first paragraph where our 
    protagonists meet
    """
    def __init__(self):
        """
        story variables
        setting, characters, weather
        """
        self.season = random.choice(seasons)
        self.grass = 'They sat on the grass in the open air, thinking this would be a day to remember.'
        self.cafe = 'They sat huddled around a warm cup of coffee, thinking this would be a day to remember.'
        self.setting_description = {
                'hot summer': self.grass,
                'rainy spring': self.grass,
                'crisp fall': self.cafe,
                'cold winter': self.cafe
                }

    def gen_meeting(self):
        """
        characters meet in setting
        s1 = June and Charlie met on a summer day.
        s2 = 
        """
        s1 = character1 + " and " + character2
        s1 += " met on a "  + self.season + " day."
        s2 = self.setting_description[self.season]
        return s1 + " " + s2

    def tell_children(self):
        """
        characters tell children about the air that day
        """
        s3 = "They would tell their children about the "
        s3 += self.season + " air the day they met."
        s4 = "They just knew."
        return s3 + " " + s4

class Second_Par():
    """
    generates second paragraph where 
    our protagonists get married
    """

    def gen_marriage(self):
        setting = ['in a church', 'on a green lawn', 'on a hill top']
        marriage_syn = ['got hitched', 'got married', 'said their vows ']
        s1 = "They " + random.choice(marriage_syn) + " " + random.choice(setting)
        s1 += " and I was sitting in the front row."
        return s1

    def describe_narrator(self):
        s2 = "My hair was floating as if "
        floating_metaphors = ["carried by a river", "a magnet were pulling the ends"]
        s2 += random.choice(floating_metaphors) + ". "
        s3 = "I smoothed it out as they kissed."
        s4 = "I wanted to " + random.choice(["yell out", "scream"])
        s4 += "go down."
        return s2 + s3 + s4 


        
class Third_Par():
    """
    generates third paragraph where
    death of character2
    """
    def __init__(self):
        self.settings = ['golf course', 'rooftop']

    def describe_scence(self):
        s1 = "The weather shifted and shifted until it was another "
        stormy_seasons = ["spring", "summer"]
        s1 += random.choice(stormy_seasons) + " day."
        s2 = "The air was heavy it was hard to " + random.choice(["breath.", "move."])
        s3 = character1 + " was on a " + random.choice(self.settings) + "."

        return s1 + s2 + s3 

    def describe_storm(self):
        s4 = "The storm was unexpected."
        s5 = "When the lightning strucks, it stopped" + character1 + "\'s heart. "
        s6 = "Hair burned to the scalp, cappillaries burst."
        s7 = " This was more than I wanted to know."

        return s4 + s5 + s6 + s7

        


if __name__ == "__main__":
    test_par1 = First_Par()
    print("\n") 
    print(test_par1.gen_meeting() + " " + test_par1.tell_children())
    print("\n") 
    test_par2 = Second_Par()
    print(test_par2.gen_marriage() + " " + test_par2.describe_narrator())
    print("\n") 
    test_par3 = Third_Par()
    print(test_par3.describe_scence() + " " + test_par3.describe_storm())
    print("\n") 



