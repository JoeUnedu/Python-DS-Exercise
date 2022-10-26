def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """  
    if (search_term in lst):
        frequency = [num for num in lst if num == search_term]
        return len(frequency)
    else:
        return 0