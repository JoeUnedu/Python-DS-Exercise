def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    idx_ = len(nums)

    if (idx_ > 1):
        #  2 numbers to check here !

        goal_tuples = {}
        while_idx_ = idx_ - 1
        idx = 0
        idx_gap = 0
        min_gap = -1

        while (idx < while_idx_):
            num1 = nums[idx]
            for num in nums[(idx + 1):]:
                idx_gap += 1
                if (num1 + num == goal):
                    # register the pair, providing a pair does not exist
                    # for this gap (meaning another pair reached the goal first)
                    if (idx_gap not in goal_tuples):
                        goal_tuples[idx_gap] = (num1, num)
                        # check whether index gap is the smallest gap
                        if (min_gap < 0):
                            # first time set
                            min_gap = idx_gap
                        else:
                            if (idx_gap < min_gap):
                                min_gap = idx_gap

            idx += 1
            idx_gap = 0
        # end while

        # anything?
        if (len(goal_tuples) > 0):
            return goal_tuples[min_gap]

    # return when only one number provided in nums or when
    #  no 2 pairs of numbers reach goal.
    return ()
