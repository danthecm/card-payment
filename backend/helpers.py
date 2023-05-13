def validate_length(value, min: int, max: int):
    """
    Validates the length of the given input

    Args:
    value: The input value must be a string or an integer
    min: The minimum length to validate against
    max: The maximum length to validate against
    """
    if not isinstance(value, (int, str)):
        raise ValueError("Value must be an integer or a string")
    value = str(value)
    if len(value) < min or len(value) > max:
        return False
    return True
