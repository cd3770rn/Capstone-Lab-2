def titlecase(word):
    word = word.lower()
    word = word.capitalize()
    return word

def display_banner():
    '''Display program name in banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def camelCase():
    
    display banner()
    
    toParse = input("Enter a senstence to parse to Camel Case: ")
    words = toParse.split(" ")
    parsed = ""
    for word in words:

        # All words that are not the first word should be capitalized
        if words.index(word) != 0:
            word = word.lower()
            word = titlecase(word)

        # The first word should be lowercase
        else:
            word = word.lower()

        parsed += word

    print(parsed)

camelCase()
