
# coding: utf-8

# In[6]:

import random

"""
SEASONS: randomly generates a dictionary of seasons-by-plot-section for story 1
"""

def gen_seasons():
    plot_order = ['opening', 'action1', 'surprise', 'action2', 'action3', 
                  'reaction', 'action4', 'action5', 'action6']

    opening_season = ('summer', 'fall', 'winter', 'spring')
    s = random.choice(opening_season)

    # get lists for orders depending on opening season
    if s == 'summer':
        season_order = ['summer', 'fall', 'summer', 'summer', 'summer', 
                        'summer', 'fall', 'summer', 'winter']
    if s == 'fall':
        season_order = ['fall', 'winter', 'fall', 'fall', 'fall', 
                        'fall', 'winter', 'fall', 'spring']            
    elif s == 'winter':
        season_order = ['winter', 'spring', 'winter', 'winter', 'winter', 
                        'winter', 'spring', 'winter', 'summer']
    elif s == 'spring':
        season_order = ['spring', 'summer', 'spring', 'spring', 'spring', 
                        'spring', 'summer', 'spring', 'fall']

    season = dict(zip(plot_order, season_order))

    return season


"""
THEME:  generates a dictionary of theme elements based on supplied word
"""
def gen_theme(noun):
    
    if noun == "relationship":
        noun = "love"
        verb = "love"
        adj = "romantic"
        adj_question = "fragile" 
        phrase = "the air was sucked out of possessive lungs"
        protag_condition = "to be alone"
        resolution_adj = "hopeful"

        theme = {'noun': noun, 
                 'verb': verb, 
                 'adj': adj, 
                 'adj_question': adj_question, 
                 'phrase': phrase, 
                 'protag_condition': protag_condition,
                 'resolution_adj': resolution_adj
                }
        
    return theme


"""
SYMBOLS:  generates a dictionary of symbols based on supplied word
"""
def gen_symbols(noun):

    if noun == "relationship":
        noun = "box"
        assoc_noun = "bookcase"
        adj = "stone"
        adj_temp = "cool"
        adj_weight = "heavy"
        adj_weight_opposite = "light"
        
        symbol = {'noun': noun,
                  'assoc_noun': assoc_noun, 
                  'adj': adj, 
                  'adj_temp': adj_temp, 
                  'adj_weight': adj_weight, 
                  'adj_weight_opposite': adj_weight_opposite
                 }

    return symbol


"""
FOR ACTION 1 & SURPRISE SECTIONS: generates a dictionary of elements that are used in 
Action1 section and Surprise Event section, based on supplied noun
"""
def gen_action1_and_surprise(noun):
    
    if noun == "relationship":
        action1_vb = "got married"
        action1_vb_entail_vb = "wasn't invited"
        action1_vb_addtl_ch = "the groom"
        action1_vb_addtl_ch_possession = "a condo"
        surprise_n = "death"
        surprise_v = "died"
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


