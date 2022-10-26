def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    no_true_element = [
        istruthy for istruthy in lst if (not(not(istruthy)))]

    return no_true_element