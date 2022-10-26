from typing import List


def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # lsit will arange the phrase "awesome" to a list such as this: 'a' w' e' s' o' m' e'
    reverse_list = list(phrase)  
    # the list will be reversed to :  'e' m' o' s' e' w' a' by the function 
    reverse_list.reverse()
    # "".join :Join all items one by one in a reverse_list into a
    # string, using "" character 
    # we need the join function to join it back to "emosewa" as a proper string 
    # it is no longer a list but a string per join function
    x = "".join(reverse_list)
    return x
print('The original string is: awesome')
print("The reverse_string is : ", end="")
print(reverse_string("awesome"))