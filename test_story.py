"""
tests story
"""

import story, par1, par2

noun_prompt = "dog"
our_story = story.Story(noun_prompt)
story_text = our_story.author_story()

def test_story():
    # story length
    assert len(story_text) > 100
    assert "." in story_text
    # add contains noun prompt?


def test_par1():
    # contains character 1
    assert our_story.characters[0] in our_story.par1
