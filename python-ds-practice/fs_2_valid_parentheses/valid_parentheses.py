def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    
    
    if ((len(parens) > 0) and (len(parens) % 2 == 0)):
        paren_ = {"(": 1, ")": -1}
        paren_total = 0
        for paren in parens:
            paren_total = paren_total + paren_[paren]
            if paren_total < 0:
                return False

        if (paren_total == 0):
            return True

    return False