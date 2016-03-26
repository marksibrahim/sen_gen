"""
generate first paragraph of a story 
based on microdoc
"""

import random
seasons = ['hot summer', 'cold winter', 'rainy spring', 'crisp fall']
grass = 'They sat on the grass in the open air, thinking this would be a day to remember.'
cafe = 'They sat huddled around a warm cup of coffee, thinking this would be a day to remember.'
setting_description = {
        'hot summer': grass,
        'rainy spring': grass,
        'crisp fall': cafe,
        'cold winter': cafe
        }

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
        s2 = setting_description[self.season]
        return s1 + " " + s2

    def tell_children(self):
        """
        characters tell children about the air that day
        """
        s3 = "They would tell their children about the "
        s3 += self.season + " air the day they met."
        s4 = "They just knew."
        return s3 + " " + s4


if __name__ == "__main__":
    test_par = First_Par()
    print(test_par.gen_meeting() + " " + test_par.tell_children())



