from nose.tools import *
from ex49.parser import ParserError, Sentence, Parser

def test_sentences():
    sentence = Parser().parse_sentence([('noun', 'Zed'), ('verb', 'kicks'), ('direction', 'north')])
    assert_equal(sentence.subject, 'Zed')
    assert_equal(sentence.verb, 'kicks')
    assert_equal(sentence.number, 1)
    assert_equal(sentence.object, 'north')
    sentence = Parser().parse_sentence([('verb', 'kicks'), ('number', 3), ('direction', 'north')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kicks')
    assert_equal(sentence.number, 3)
    assert_equal(sentence.object, 'north')
    sentence = Parser().parse_sentence([('noun', 'Mary'), ('verb', 'kicks'), ('stop', 'it'), ('direction', 'north')])
    assert_equal(sentence.subject, 'Mary')
    assert_equal(sentence.verb, 'kicks')
    assert_equal(sentence.number, 1)
    assert_equal(sentence.object, 'north')
    sentence = Parser().parse_sentence([('verb', 'kicks'), ('direction', 'north'), ('direction', 'is'), ('direction', 'am')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kicks')
    assert_equal(sentence.number, 1)
    assert_equal(sentence.object, 'north')
    sentence = Parser().parse_sentence([('verb', 'kicks'), ('noun', 'ball')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kicks')
    assert_equal(sentence.number, 1)
    assert_equal(sentence.object, 'ball')

def test_errors():
    sentence = [('noun', 'Mary'), ('verb', 'takes'), ('stop', 'and'), ('verb', 'kicks'), ('direction', 'north')]
    assert_raises(ParserError, Parser().parse_sentence, sentence)
