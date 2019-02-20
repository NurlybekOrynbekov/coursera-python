def is_braces_sequence_correct(seq: str) -> bool:
    """
    Check corretness of braces sequence in statment
    >>> is_braces_sequence_correct("()(())")
    True
    >>> is_braces_sequence_correct("()[()]")
    True
    >>> is_braces_sequence_correct(")")
    False
    >>> is_braces_sequence_correct("[()")
    False
    >>> is_braces_sequence_correct("[(])")
    False
    """
    stack = []
    correspondent = dict(zip("([{", ")]}"))
    for brace in seq:
        if brace in "([{":
            stack.append(brace)
            continue
        elif brace in ")]}":
            if not stack:
                return False
            left = stack.pop()
            if correspondent[left] != brace:
                return False

        return not stack



if __name__ == '__main__':
    import doctest
    doctest.testmod()