directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['bear', 'door', 'princess', 'cabinet']

def scan(words):
    words = words.split()
    result = []

    for word in words:
        word_lower = word.lower()
        try:
            # See if it is a number
            num = int(word_lower)
            result.append(("number", num))
        except ValueError:
            # Check if direction
            if word_lower in directions:
                result.append(('direction', word))
            elif word_lower in verbs:
                result.append(('verb', word))
            elif word_lower in stops:
                result.append(('stop', word))
            elif word_lower in nouns:
                result.append(('noun', word))
            else:
                result.append(('error', word))

    return result
