class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, number, object):
        # Remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.number = number[1]
        self.object = object[1]

def peek(word_list):
    """Takes in a list of tuples and returns the first tuple in the list.
    Returns None if list is empty."""
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """Takes in a list of tuples and the expecting type.
    Removes the first tuple from the list and returns the word if it is of the expected type.
    Else, return None if list is empty or if the first word is not of the expected type."""
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """Takes in a list of tuples and word type.
    Modifies the list by removing the words of that word type."""
    while peek(word_list) == word_type:
        match(word_list, word_type)

class Parser(object):
    def parse_verb(self, word_list):
        """Takes in a word list.
        Removes all 'stop' types in list, then checks if first word in the list is a verb.
        Removes first word in the list if it is a verb.
        Else, raises ParserError"""
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_number(self, word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'number':
            return match(word_list, 'number')
        else:
            word_list.insert(0, ('number', 1))
            return match(word_list, 'number')

    def parse_object(self, word_list):
        """Takes in a word list.
        Removes all 'stop' types in list, then checks if first word in the list is a noun or direction.
        Removes first word in the list if it is a noun or direction.
        Else, raises ParserError."""
        skip(word_list, 'stop')
        next = peek(word_list)

        if next == 'noun':
            return match(word_list, 'noun')
        if next == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(self, word_list, subj):
        """Takes in a list of tuples and the subject as a tuple.
        Retrieves verb and object, then returns the words as a Sentence object."""
        verb = self.parse_verb(word_list)
        number = self.parse_number(word_list)
        obj = self.parse_object(word_list)

        return Sentence(subj, verb, number, obj)

    def parse_sentence(self, word_list):
        """Takes in a list of tuples.
        Removes all 'stop' types in list.
        Checks if first word is a noun or a verb.
        If it is a noun, return Sentence.
        If it is a verb, return Sentence with player as noun.
        Else raises ParserError."""
        skip(word_list, 'stop')

        start = peek(word_list)

        if start == 'noun':
            subj = match(word_list, 'noun')
            return self.parse_subject(word_list, subj)
        elif start == 'verb':
            # Assume the subject is the player then
            return self.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not:", start)
