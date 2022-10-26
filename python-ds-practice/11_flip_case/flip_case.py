def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_t = {to_swap.lower(), to_swap.upper()}

    flip_it = [
        letter.swapcase() if letter in swap_t else letter for letter in phrase]

    return "".join(flip_it)