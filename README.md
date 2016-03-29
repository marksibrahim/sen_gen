# sen_gen
## Goal 
* extract sentence from generated text
    * sanity grammar check sentence
* accept or reject sentence based on fit with the rest of story theme
    * as well as tense

## Building the Story

Theme: greed is downfall

Setup: 
P: protagonist
    P = proper name + adj
G: goal
    G = [list based on theme]
    * in here there should an action and an objective
O: opponent
    O = proper name + adj (based on goal)

sample list of goals
objective = [wealth: bit coin, rare coin collection, stock market investments, 
real estate, mortgage, coffee trade]
actions = [theft, deal, money launder, trade]

setting = [bank]

hurdle = [regulation, illegality, market crash]


### Story Structure : love story

1. introduce protagonist + setting
    proper name + adj + lives + proper place.
2. introduce goal
    a. protagonist unfulfilled:
    maybe loneliness
    P + feeling + syn to lonely.
    There existed a beautiful [proper name].
3. seemingly successful pursuit of goal
    P meets G in [setting]
    agree to see each other again.
4. introduce oppponent
    Introduce opponent.
    Opponent sways G.
5. overcome challenge
    P + feels defeated
    P + verb + (courage) 
6. resolution
    G + P live happily ever after.



## Data
* Corpus of 3.5 million words from short stories.

## Ideas
- scrap web source of text
- use thesaurus to identify emotional content

* short story length 4,000 words 
* to measure emotional content using nltk sentiment

* when generating story based on noun use thesaurus to lookup synonymous terms in our corpus.
    * swap terms throughout generated text.

* rather than fit a story to a shape, we can construct lots of stories and select 
the one that fits the shape we desire.

* maybe through in an unconventional element into the story (picture of a letter or the like)

* perhaps open with a quote from a famous author that fits our shape story

### emotions
- happy
- worried
- mad
- surprised
- sad
perhaps incorporate emotional equations, i.e. combine emotions for a nuanced emotion. 

### Themes and Story Parts
''' Python
    themes = ["love", "death", "jealousy", "corruption"]

    openings = ["meeting"]
    first_actions = ["marriage"]
    first_reversals = ["death"]

    first_reactions = ["funeral"]
    # about first reaction and theme
    dialogue_theme = ["love dialogue"]
    closing_first_reactions = ["burial"]
    feelings_first_reactions = ["sadness"]

    second_actions = ["meeting"]
    # more about theme, surprising
    dialogue_reversals = ["love dialogue"]

    third_actions = ["second marriage"]
    fourth_actions = ["meeting"]
    dialogue_conclusions = ["love"]
    resolutions = ["love"]
'''

## Things to Ponder
* how do we keep track of characters?
* themes? emotional content to create flow?
    * use imagery or setting to create a consistent theme
    * hero and villain characters (and side characters to go along with them)

## Accomplished
* successfully generating sentences using a Markov chain of 3
    * chains of 4 too closely resemble original corpus

## Resources
http://blog.ayoungprogrammer.com/2015/09/a-simple-artificial-intelligence.html


