# sen_gen
## Goal 
* extract sentence from generated text
    * sanity grammar check sentence
* accept or reject sentence based on fit with the rest of story theme
    * as well as tense

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


