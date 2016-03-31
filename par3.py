
# coding: utf-8

# In[ ]:

"""
generates first paragraph based on elements in story.py

TO CHANGE IN MARK's CODE -- season with no modifier, e.g., "summer"
ADD TO STORY.PY: object_pronoun for each character

NOTE:  put all lists and dictonaries in STORY.PY

"""

import story
import random
from nltk.corpus import wordnet as wn

class Par3(s1_season, s2, character1, character2, character3):

    season = s1_season

    # The weather shifted and shifted until it was another summer day.    
    phrase = ['The weather shifted and shifted', 'The year rolled through the seasons', 'Time passed, the weather shifted,', 'The year crept by', 'Season after season,the year slid in its circle']
    s13 = random.choice(phrase) + " until it was another " + season + " day. "

    # The air was so heavy it was hard to breath.
    s14 = s2

    # Charlie was golfing.
    sports_verbs = {
        'spring': 'running',
        'spring': 'bird watching',
        'spring': 'mushroom hunting',
        'summer': 'biking', 
        'summer': 'kayaking', 
        'summer': 'golfing', 
        'fall': 'rock climbing',
        'fall': 'fishing',
        'fall': 'playing tennis',
        'winter': 'snowshoeing',
        'winter': 'skiing',
        'winter': 'snow boarding',
        }    
    s15 = character2.name + " was " + random.choice(sports_verbs[season]) + ". "
    
    # That's what June told me.
    s16 = "That's what " + character1.name + " told " + character3.object_pronoun
    
    # The storm was so unexpected, there was no reason to believe it would come.
    unexpected = ['unexpected', 'swift and astonishing', 'sudden']    
    s17 = "The storm was so " + random.choice(unexpected) + ", " + "there was no reason to believe it would come. "

    # When the lightning struck, it stopped his heart.
    s18 = "When the lightning struck, it stopped his heart. "
    
    # His hair was burned to the scalp, his skin tattooed with fractals as his capillaries burst.
    s19 = "His hair was burned to the scalp, his skin tattooed with fractals as his capillaries burst. "
    
    # That was more than I wanted to know.
    s20 = "That was more than I wanted to know."
    
    par3 = s13 + s14 + s15 + s16 + s17 + s18 + s19 + s20
    
    return par3
    
class Par4(s1_season, character1, character3):
    
    season = s1_season
    
    # I sat in the first row at the funeral.
    s21 = character3.pronoun + " sat in the first row at the funeral."
    
    # June was my best friend.
    if character1.gender == 'male':
        relationship = ["best friend", "brother", "cousin", "business partner"]
    else:
        relationship = ["best friend", "sister", "cousin", "business partner"]
        
    relation = random.choice(relationship)
    
    s22 = character1.name + " was " + character3.possessive_pronoun + random.choice(relationship)
    
    if relation == 'business partner' and character1.gender == 'male':
        s22 = s22 + "but he was more than that."
    elif relation == 'business partner' and character1.gender == 'female':  
        s22 = s22 + "but she was more than that."
    else:
        s22 = s22 + "."

    # The ground was soft because it had been raining.
    # My heels sucked into the mud, not wanting to let go.
    
    if season == "winter":
        ground_state1 = "felt soft"
        weather_verb = "snowing"
        feet = "boots sunk "
        ground_state2 = "snow"
    else:
        ground_state1 = "was soft"
        weather_verb = "raining"
        feet = "heels sucked "
        ground_state2 = "mud"

    s23 = "The ground " + ground_state1 + " because it has been " + weather_verb + "."
    
    s24 = character3.possessive_pronoun + " " + feet + " into the " + ground_state2 + ", not wanting to let go."
    
    par4 = s21 + s22 + s23 + s24
    
    return par4

