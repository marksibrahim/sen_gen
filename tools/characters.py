from nltk.corpus import names
import random

class Character():

    '''
    Call as follows:
        ch = Character('male', 'third', False)
        ch1 = ch.create_character()
        ch1['first_name'], etc.
    '''

    def __init__(self, gender, pov, plural):

        self.gender = gender
        self.pov = pov
        self.plural = plural

    def create_character(self):
        '''
        returns a character name based given gender
        '''
        if self.gender == 'male':
            first_name = random.choice([(name) for name in names.words('male.txt')])
            ch = {'gender': 'male'}
        else:
            first_name = random.choice([(name) for name in names.words('female.txt')])
            ch = {'gender': 'female'}
            
        ch = ch.update({'first_name': first_name})

        '''
        returns pronouns based on:
        - gender: male, female, neuter
        - pov (point of view): first, second, third
        - plural: True or False
        '''

        if self.pov == 'first' and self.plural == False:
            pronouns = {
            'pronoun': 'I', 
            'object_pn': 'me', 
            'possessive': 'my', 
            'possessive_pn': 'mine', 
            'reflexive_pn': 'myself'
            }
            ch.update(pronouns)

        elif self.pov == 'second' and self.plural == False:
            pronouns = {
            'pronoun': 'you', 
            'object_pn': 'you', 
            'possessive': 'your', 
            'possessive_pn': 'yours', 
            'reflexive_pn': 'yourself'
            }
            ch.update(pronouns)

        elif self.gender == 'male' and self.pov == "third" and self.plural == False:
            pronouns = {
            'pronoun': 'he', 
            'object_pn': 'him', 
            'possessive': 'his', 
            'possessive_pn': 'his', 
            'reflexive_pn': 'himself'
            }
            ch.update(pronouns)

        elif self.gender == 'female' and self.pov == 'third' and self.plural == False:
            pronouns = {
            'pronoun': 'she', 
            'object_pn': 'her', 
            'possessive': 'her', 
            'possessive_pn': 'hers', 
            'reflexive_pn': 'herself'
            } 
            ch.update(pronouns)

        elif self.gender == 'neuter' and self.pov == 'third' and self.plural == False:
            pronouns = {
            'pronoun': 'it', 
            'object_pn': 'it', 
            'possessive': 'its', 
            'possessive_pn': '', 
            'reflexive_pn': 'itself'
            }
            ch.update(pronouns)

        elif self.pov == 'first' and self.plural == True:
            pronouns = {
            'pronoun': 'we', 
            'object_pn': 'us', 
            'possessive': 'our', 
            'possessive_pn': 'ours', 
            'reflexive_pn': 'ourselves'
            }
            ch.update(pronouns)

        elif self.pov == 'second' and self.plural == True:
            pronouns = {
            'pronoun': 'you', 
            'object_pn': 'you', 
            'possessive': 'your', 
            'possessive_pn': 'yours', 
            'reflexive_pn': 'yourselves'
            }
            ch.update(pronouns)

        elif self.pov == 'third' and self.plural == True:
            pronouns = {
            'pronoun': 'they', 
            'object_pn': 'them', 
            'possessive': 'their', 
            'possessive_pn': 'theirs', 
            'reflexive_pn': 'themselves'
            }
            ch.update(pronouns)

        return ch


class CharacterDetails():

    def __init__(self):

        self.body_part1 = "hair"
        self.body_part2 = "hands"
        

    def create_character(self):
    