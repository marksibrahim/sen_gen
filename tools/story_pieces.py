import random

"""
SEASONS: randomly generates a dictionary of seasons-by-plot-section for story 1
"""

def gen_seasons():
    plot_order = ['action1', 'action2', 'action3', 'action4', 'action5', 'action6', 
                  'action7', 'action8', 'action9']

    opening_season = ('summer', 'fall', 'winter', 'spring')
    s = random.choice(opening_season)

    # get lists for orders depending on opening season
    if s == 'summer':
        season_order = ['summer', 'fall', 'summer', 'summer', 'summer', 
                        'fall', 'fall', 'winter', 'spring']
    if s == 'fall':
        season_order = ['fall', 'winter', 'fall', 'fall', 'fall', 
                        'winter', 'winter', 'spring', 'summer']            
    elif s == 'winter':
        season_order = ['winter', 'spring', 'winter', 'winter', 'winter', 
                        'spring', 'spring', 'summer', 'fall']
    elif s == 'spring':
        season_order = ['spring', 'summer', 'spring', 'spring', 'spring', 
                        'summer', 'summer', 'fall', 'winter']

    season = dict(zip(plot_order, season_order))

    return season


"""
SETTINGS
"""

def gen_setting_sentences():

    setting_sAB = {
        'fall': {'sA': "the wind was blowing so hard, ", 
                 'sB': "the air rushed into their mouths until they couldn't breathe", 
                 'sC': "the wind was blowing so hard it sucked the breath out of the sparrows"},  
      'winter': {'sA': "it was so cold the walnut trees were exploding like gunshots", 
                 'sB': "the air was so thin it was hard to breath"},  
      'spring': {'sA': "the sky was stuffed round with rain clouds", 
                 'sB': "the air was a shimmering gray that was hard to look at"}, 
      'summer': {'sA': "it was so hot the grass was laying down yellow in exhaustion", 
                 'sB': "the air was so heavy it was hard to breath"}
                   }

    return setting_sAB


"""
PLACES
"""
def gen_event(story_type):

    if story_type == "1" or story_type == "2":

        event = {'relationship': {  
                      'event1': "wedding", 
                    'event1_v': "was sitting", 
                      'event2': "at the funeral", 
                    'event2_v': "sat", 
                    'location': "in the first row", 
                   'event2_v2': "buried", 
                        'noun': "ashes"
                   }
                }

    return event


"""
THEME:  generates a dictionary of theme elements based on supplied word
theme[]
"""
def gen_theme(story_type):
    
    if story_type == "1" or story_type == "2":

        noun = "love"
        n_adj = "short"
        verb = "love"
        adj = "romantic"
        adj_question = "fragile" 
        phrase = "the air was sucked out of possessive lungs"
        protag_condition = "to be alone"
        action1_adj = "hopeless"
        resolution_adj = "hopeful"

        theme = {'noun': noun, 
                 'n_adj': n_adj, 
                 'verb': verb, 
                 'adj': adj, 
                 'adj_question': adj_question, 
                 'phrase': phrase, 
                 'protag_condition': protag_condition,
                 'action1_adj': action1_adj, 
                 'resolution_adj': resolution_adj
                }
        
    return theme


"""
SYMBOLS:  generates a dictionary of symbols based on supplied word
symbol[]
"""
def gen_symbols(story_type):
    
    if story_type == "1" or story_type == "2":

        noun = "box"
        assoc_noun = "bookcase"
        adj = "stone"
        adj_aux = "small"
        adj_prop = "hollow in the center"
        adj_temp = "cool"
        adj_weight = "heavy"
        adj_weight_opposite1 = "weightless"
        adj_weight_opposite2 = "light"
        excuse = "the weather"

        symbol = {'noun': noun,
                  'assoc_noun': assoc_noun, 
                  'adj': adj,
                  'adj_aux': adj_aux, 
                  'adj_prop': adj_prop, 
                  'adj_temp': adj_temp, 
                  'adj_weight': adj_weight, 
                  'adj_weight_opposite1': adj_weight_opposite1, 
                  'adj_weight_opposite2': adj_weight_opposite2, 
                  'excuse': excuse
                 }

    return symbol


"""
FOR ACTION 1 & SURPRISE SECTIONS: generates a dictionary of elements that are used in 
Action1 section and Surprise Event section, based on supplied noun
a1_surprise[]
"""
def gen_action1_and_surprise(story_type):
    
    if story_type == "1" or story_type == "2":

        action1_vb = "got married"
        action1_vb_entail_vb = "wasn't invited"
        action1_vb_addtl_ch = "the groom"
        action1_vb_addtl_ch_possession = "a condo"
        surprise_n = "death"
        surprise_v = "die"
        surprise_opposite_adj = "lucky"

        a1_surprise = {'action1_vb': action1_vb, 
                       'action1_vb_entail_vb': action1_vb_entail_vb, 
                       'action1_vb_addtl_ch': action1_vb_addtl_ch, 
                       'action1_vb_addtl_ch_possession': action1_vb_addtl_ch_possession, 
                       'surprise_n': surprise_n,
                       'surprise_v': surprise_v,
                       'surprise_opposite_adj': surprise_opposite_adj
                      }

    return a1_surprise


