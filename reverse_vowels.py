def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'AEIOUYaeiouy'

    letter_list = []
    vowel_list = []

    for letter in s:
        if vowels.find(letter) == -1:
            letter_list.append(letter)
        else:
            vowel_list.append(letter)
            letter_list.append('#')

    vowel_list.reverse()

    vowel_index = 0
    letter_index = 0

    for letter in letter_list:
        if letter == '#':
            letter_list[letter_index] = vowel_list[vowel_index]
            vowel_index += 1
        letter_index += 1

    return ''.join(letter_list)

