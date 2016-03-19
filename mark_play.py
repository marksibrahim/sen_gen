"""
generate first paragraph of a story 
based on microdoc
"""

import random
seasons = ['hot summer', 'cold winter', 'rainy spring', 'crisp fall']

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


    def gen_meeting(self):
        """
        characters meet in setting
        s1 = June and Charlie met on a summer day.
        s2 = 
        """
        s1 = "June and Charlie met on a "  + self.season + " day."
        s2 = " "
        return s1


if __name__ == "__main__":
    test_par = First_Par()
    print(test_par.gen_meeting())



