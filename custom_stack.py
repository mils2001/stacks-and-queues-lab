
def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    stack = []
    matching_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in '({[':
            # Push opening brackets onto the stack.
            stack.append(char)

        elif char in ')}]':
            # Closing bracket needs a matching opening bracket.
            if not stack or stack[-1] != matching_pairs[char]:
                return False

            # Remove the matching opening bracket.
            stack.pop()

    # All opening brackets must have been matched.
    return len(stack) == 0
