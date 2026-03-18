def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
     # Mapping Roman symbols to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    # Iterate through the string character by character
    for i in range(len(roman)):
        # Get the integer value of the current Roman symbol
        current_value = roman_map[roman[i]]

        # Look ahead: if the next symbol is larger, subtract the current
        if i + 1 < len(roman) and current_value < roman_map[roman[i+1]]:
            total -= current_value
        else:
            # Otherwise, add the current symbol
            total += current_value

    return total

# Example usage:
# print(solution("MCMXC"))  # Output: 1990
# print(solution("MMVIII")) # Output: 2008

# Create a function that takes a Roman numeral as
# its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.