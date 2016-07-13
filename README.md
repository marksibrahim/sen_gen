# Short Story by AI

goal: generate a short story of tragic love based on a noun prompt
* code submitted to the [Turing Test in Creative Arts](http://bregman.dartmouth.edu/turingtests/node/1) hosted by Dartmouth College

## Usage

### Requirements
* Install: NLTK + [WordNet](http://www.nltk.org/howto/wordnet.html) corpus
```python
$ sudo pip install -U nltk
```

To run :
```python
$ python story.py "dog"
```
> And then the man would say, "The dog recoiled, tail between his legs," which made no sense. Yet she couldn't shake the feeling that they pointed to the box.

Or a noun + adj: 
```python
$ python story.py "dirty subway"
```
> A man would say, "“Where’s the subway?” Jerry said."  And I would reply, "Lily was in the subway." It was unsettling. Why was I dreaming about a subway? I thought it was because my life seemed so just outside of my reach.


## Implementation 
* corpus of 1000 short stories
* generate sentences based on theme and noun prompt using tri-gram Markov Chains 
  * 4-grams mimick the corpus text too closely; bi-grams produce jumbled words
  * implementation based on Gist: https://gist.github.com/dellis23/6174914

## Elements of a Story

### Characters

* assign gender, age, name for each character
* names based on census names list (randomly assigned)

### Setting

* create season information and relationship to weather
  * description of setting based on weather
* synonyms are swaped for word variety 

### Plot 

EVENTS:  actions at places

OPENING: Meeting = Characters + action (“meeting” in this case) + setting -> ACTION 1 

Action | Relation
------------ | -------------
ACTION 1:    Marriage 1     |   relates to:  ACTION 7
ACTION 2:    Death           | leads to ACTION 3
ACTION 3:    Funeral          |  leads to ACTION 4
DIALOGUE 1:  at Funeral      |  relates to ACTION 3
ACTION 4:    Burial            |relates to ACTION 3
ACTION 5:    Reaction to death  |  relates to ACTION 2 & THEME
ACTION 6:    Meeting 1        | lead to dialogue
DIALOGUE 2:  at Meeting 1   |     relates to OPENING, ACTION 1, ACTION 2 & THEME
ACTION 7:    Marriage 2       | relates to ACTION 1 & DIALOGUE 2
ACTION 8:    Meeting 2      |  relates to ACTION 6 
DIALOGUE 3:  at Meeting 2  |    relates to DIALOGUE 2 & THEME
RESOLUTION:  Emotions, thoughts of protagonist at the end  | or ultimate situation

## Future

* add structural variety + themes
* more nuianced parsing of the input noun (wordnet categories)
* additional strategically placed markov sentences
    * check grammar and word sense
