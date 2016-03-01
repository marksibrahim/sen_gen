import story

test_story = story.Story()

def test_sentence():
    """
    tests whether the generate sentence method returns a sentence
    by searching for ? ! or .
    """
    sen_delimeter = ["?", "!", "."]
    test_sentence = test_story.generate_sentence()
    
    assert any(x in test_sentence for x in sen_delimeter)


