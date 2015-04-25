def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, forbidden):
    for item in word:
        if item in forbidden:
            return False
    return True

def uses_only(word, required):
    for letter in word:
        if letter not in required:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
    
print has_no_e('Feelings')
print has_no_e('Hat')

print "Hello"

