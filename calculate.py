def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """

    def make_total_int(total_num):
        if make_int == True:
            total_num = int(total_num)
            return message + ' ' + str(total_num)
        else:
            return message + ' ' + str(total_num)


    if operation == 'add':
        total = a + b
        return make_total_int(total)

    elif operation == 'subtract':
        total = a - b
        return make_total_int(total)

    elif operation == 'multiply':
        total = a * b
        return make_total_int(total)

    elif operation == 'divide':
        total = a / b
        return make_total_int(total)

    else:
        return None