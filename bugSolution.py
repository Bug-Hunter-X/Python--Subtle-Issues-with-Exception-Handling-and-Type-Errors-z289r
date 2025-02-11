def function_with_improved_error_handling(a, b):
    """This function performs division and handles errors more robustly.
    Args:
        a: The numerator (must be a number).
        b: The denominator (must be a number, not zero).
    Returns:
        The result of the division if successful, otherwise None.
    """
    assert isinstance(a,(int, float)), "Input 'a' must be a number"
    assert isinstance(b,(int, float)), "Input 'b' must be a number"
    assert b != 0, "Input 'b' cannot be zero"
    try:
        result = a / b
        return result
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage demonstrating more robust handling
print(function_with_improved_error_handling(10, 0)) #AssertionError
print(function_with_improved_error_handling(10, 2))  # Returns 5.0
print(function_with_improved_error_handling("10", 2)) #AssertionError
print(function_with_improved_error_handling(10, "2")) #AssertionError