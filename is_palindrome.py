def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    clean_phrase = phrase.replace(' ','')

    lst = list(clean_phrase.lower())
    rev_lst = lst.copy()
    rev_lst.reverse()

    if lst == rev_lst:
        return True
    else:
        return False