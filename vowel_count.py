def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    low_phrase = phrase.lower()
    vowels = 'aeiou'
    vowel_dict = {}

    # for vowel in vowels:
    #     if low_phrase.count(vowel) != 0:
    #         vowel_dict[vowel] = low_phrase.count(vowel)

    for letter in low_phrase:
        if letter in vowels:
            vowel_dict[letter] = low_phrase.count(letter)

    return vowel_dict
