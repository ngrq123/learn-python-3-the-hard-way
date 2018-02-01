from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    assert_equal(lexicon.scan("back"), [('direction', 'back')])
    assert_equal(lexicon.scan("right"), [('direction', 'right')])
    result = lexicon.scan("north soUth east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'soUth'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    assert_equal(lexicon.scan("stop"), [('verb', 'stop')])
    result = lexicon.scan("go KILL eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'KILL'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    assert_equal(lexicon.scan("from"), [('stop', 'from')])
    assert_equal(lexicon.scan("at"), [('stop', 'at')])
    result = lexicon.scan("THe in of")
    assert_equal(result, [('stop', 'THe'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    assert_equal(lexicon.scan("cabinet"), [('noun', 'cabinet')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    assert_equal(lexicon.scan("djfJHD"), [('error', 'djfJHD')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
