def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_list = list(phrase)
    phrase_set = set(phrase)

    count_dict = {}

    for letter in phrase_set:
        count_dict[letter] = phrase_list.count(letter)

    return count_dict