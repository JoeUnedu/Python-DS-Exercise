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
    to_add = "add"
    to_subtract = "subtract"
    to_multiply = "multiply"
    to_divide  = "divide"
    
    to_operations = {to_add,to_subtract,to_multiply,to_divide}
    result = 0
    lower_operation = operation.lower()
    
    if(lower_operation in to_operations):
       if(lower_operation == to_add):
        result = a + b
    elif (lower_operation == to_subtract):
            result = a-b
    elif(lower_operation == to_divide):
              result = a * b
    else:
        result = a/b
        
        if make_int:
            result = int(result)
            
            return f"{message} {result}"
        else:
            return None
              
              
              