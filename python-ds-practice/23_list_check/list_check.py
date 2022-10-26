def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """


    if (len(lst)>0):
        for num in lst:
            # isinstance checks of something is a list of the item
            if(isinstance(num, list) == False):
                return False
            else:
                return True
        else:
                return False
    