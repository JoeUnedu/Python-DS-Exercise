def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_phrase = phrase.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    listofpharase = [letter.lower()
                   for letter in lower_phrase if letter in letters]
    list_reverse = listofpharase.copy()
    list_reverse.reverse()

    if (listofpharase == list_reverse):
        return True
    else:
        return False
