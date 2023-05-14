def validate_length(value, min: int, max: int):
    """
    Validates the length of the given input

    Args:
    value: The input value must be a string or an integer
    min: The minimum length to validate against
    max: The maximum length to validate against

    Returns:
    True: if the length of the input is valid
    False: if the length of the input is not valid
    """
    if not isinstance(value, (int, str)):
        raise ValueError("Value must be an integer or a string")
    value = str(value)
    if len(value) < min or len(value) > max:
        return False
    return True


def luhn_algorithm_check(value: str) -> bool:
    """
    Checks if the value matches Luhn's Algorithm

    Args:
    value: string

    Return:
    True if the value matches Luhn's Algorithm
    False if the value does not match Luhn's Algorithm
    """
    result = []
    for index, value in enumerate(reversed(value)):
        try:
            value = int(value)
        except ValueError:
            continue
        if index % 2 != 0:
            value = value * 2
            if value > 9:
                value = value - 9
        result.append(value)
    total_sum = sum(result)
    if total_sum % 10 == 0:
        return True
    return False
