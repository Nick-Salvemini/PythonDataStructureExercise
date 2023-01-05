def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letter_to_swap = to_swap.lower()
    str = []

    for letter in phrase:
        if letter == letter_to_swap:
            str.append(letter.upper())
        elif letter == letter_to_swap.upper():
            str.append(letter.lower())
        else:
            str.append(letter)
    
    return ''.join(str)