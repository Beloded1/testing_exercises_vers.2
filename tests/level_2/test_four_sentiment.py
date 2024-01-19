from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest

def test__check_tweet_sentiment__if_not_good_and_not_bad_words():
    assert check_tweet_sentiment('This string doesn"t contain any good or bad words', ['nicy', 'cool'], ['scary', 'ugly']) == None

def test__check_tweet_sentiment__if_good_and_bad_words_are_equal():
    assert check_tweet_sentiment('This is a nicy and scary string', ['nicy', 'cool'], ['scary', 'ugly']) == None

def test__check_tweet_sentiment__if_more_good_words_found():
    assert check_tweet_sentiment('This is a nicy and cool but scary string', ['nicy', 'cool'], ['scary', 'ugly']) == 'GOOD'


def test__check_tweet_sentiment__if_more_bad_words_found():
    assert check_tweet_sentiment('This is a nicy but scary and ugly string', ['nicy', 'cool'], ['scary', 'ugly']) == 'BAD'


def test__check_tweet_sentiment__if_only_good_words_found():
    assert check_tweet_sentiment('This is a nicy and cool string', ['nicy', 'cool'], ['scary', 'ugly']) == 'GOOD'


def test__check_tweet_sentiment__if_only_bad_words_found():
    assert check_tweet_sentiment('This is a scary and ugly string', ['nicy', 'cool'], ['scary', 'ugly']) == 'BAD'



def test__check_tweet_sentiment__if_invalid_input():
    with pytest.raises(AttributeError):
        check_tweet_sentiment(123, [1,2], ['scary', 'ugly'])



