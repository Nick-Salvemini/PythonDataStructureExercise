def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    new_lst=[]

    for elem in lst:
        if lst.index(elem) % 2 == 0:
            new_lst.append(elem)

    return new_lst