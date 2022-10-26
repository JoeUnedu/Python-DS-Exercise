def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_count1 = {}
    if (len(phrase) > 0):
        phrase_ = phrase.lower()

        #vowel_count_out = {letter: 0 for letter in phrase_lower}
        for letter in phrase_:
            if (letter in "aeiou"):
                count = 1 + vowel_count1.get(letter, 0)
                vowel_count1[letter] = count

    return vowel_count1



