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
    common = {}

    for num in nums:
        common[num] = common.get(num, 0) + 1
    max_val = max(common.values())
    for key, val in common.items():
        if val == max_val:
            return key