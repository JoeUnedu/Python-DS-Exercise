def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    idstart = 0
    maxtimes = len(nums)
    numtimes = 0

    while (idstart < maxtimes):
        num_test = nums[idstart]
        for num in nums[idstart:]:
            if num_test < num:
                numtimes += 1

        idstart += 1

    return numtimes