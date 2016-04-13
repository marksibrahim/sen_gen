
# coding: utf-8

# In[6]:

import random
from collections import defaultdict

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
SETTING
"""

def gen_setting_sentences():

    setting_sAB = defaultdict(dict)

    setting_sAB['fall']['sA'] = "the wind was blowing so hard, "
    setting_sAB['fall']['sB'] = "the air rushed into their mouths until they couldn't breathe"
    setting_sAB['fall']['sC'] = "the wind was blowing so hard it sucked the breath out of the sparrows"
    setting_sAB['winter']['sA'] = "it was so cold the walnut trees were exploding like gunshots, "
    setting_sAB['winter']['sB'] = "the air was so thin it was hard to breath"
    setting_sAB['spring']['sA'] = "the sky was stuffed round with rain clouds"
    setting_sAB['spring']['sB'] = "the air was a shimmering gray that was hard to look at"
    setting_sAB['summer']['sA'] = "it was so hot the grass was laying down yellow in exhaustion"
    setting_sAB['summer']['sB'] = "the air was so heavy it was hard to breath"

    return setting_sAB
 

"""
THEME:  generates a dictionary of theme elements based on supplied word
theme[]
"""
def gen_theme(noun):
    
    if noun == "relationship":
        noun = "love"
        verb = "love"
        adj = "romantic"
        adj_question = "fragile" 
        phrase = "the air was sucked out of possessive lungs"
        protag_condition = "to be alone"
        action1_adj = "hopeless"
        resolution_adj = "hopeful"

        theme = {'noun': noun, 
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
def gen_symbols(noun):

    if noun == "relationship":
        noun = "box"
        assoc_noun = "bookcase"
        adj = "stone"
        adj_temp = "cool"
        adj_weight = "heavy"
        adj_weight_opposite = "light"
        excuse = "the weather"
        
        symbol = {'noun': noun,
                  'assoc_noun': assoc_noun, 
                  'adj': adj, 
                  'adj_temp': adj_temp, 
                  'adj_weight': adj_weight, 
                  'adj_weight_opposite': adj_weight_opposite
                  'excuse': excuse
                 }

    return symbol


"""
FOR ACTION 1 & SURPRISE SECTIONS: generates a dictionary of elements that are used in 
Action1 section and Surprise Event section, based on supplied noun
a1_surprise[]
"""
def gen_action1_and_surprise(noun):
    
    if noun == "relationship":
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


