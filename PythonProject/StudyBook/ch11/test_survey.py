from survey import AnonymousSurvey

def test_story_single_response():

    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses