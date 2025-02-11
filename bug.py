def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example usage that can lead to subtle issues
print(function_with_uncommon_error(10, 0))  # Prints error and returns None
print(function_with_uncommon_error(10, 2))  # Returns 5.0
print(function_with_uncommon_error("10", 2)) #Prints Error: Invalid input type and return None
print(function_with_uncommon_error(10, "2")) #Prints Error: Invalid input type and return None
