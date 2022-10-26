def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    #  The len() function returns the number of items in an object.
    # if the object is a string it returns the number of characters
    if (len(lst) > 0):
        # lst[2] may return the last element but is not very logical if the array expands 
        # in list hence -1 is prefered
        return lst[-1]
    else:
        return None
    
    
print(f"last_element([1, 2, 3]): {last_element([1, 2, 3])}")
    