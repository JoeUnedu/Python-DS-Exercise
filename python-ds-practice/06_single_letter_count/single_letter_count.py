def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    
    new_letter = letter.lower()
    new_word = word.lower()
    if( new_letter in new_word):
        for char in new_word:
            if(char == new_letter):
                     new_List = new_letter
            return len(new_List)
        else:
            return 0
        
print (single_letter_count("Hello World","z"))