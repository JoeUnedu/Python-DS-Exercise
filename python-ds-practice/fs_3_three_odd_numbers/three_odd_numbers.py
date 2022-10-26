def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    nums_ = len(nums)
    if (nums_ > 2):
   
        nums_ = nums_ - 2
        i = 0
        three_odd = 0
        while (i < nums_):
            three_odd = nums[i] + nums[i + 1] + nums[i + 2]
            if (three_odd % 2 == 1):
            
                return True

            i += 1

    return False