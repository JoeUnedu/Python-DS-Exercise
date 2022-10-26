def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
# most num  is holding numbers that occurred the most
    most_num = ""
    # most_frequency is holding the most TOTAL times a number occured.
    most_frequency = 0
    num_frequency = {num: 0 for num in nums}
    for num in nums:
        num_frequency[num] += 1
        # if  the number  of times num occur exceed the amount in most_frequency
        if (num_frequency[num] >= most_frequency):
            # if it is greater , take the number and put it in the most_num
            most_num = num

    return most_num