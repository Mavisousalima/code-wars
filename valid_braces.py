def valid_braces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


assert valid_braces("(){}[]") == True
assert valid_braces("([{}])") == True
assert valid_braces("(}") == False
assert valid_braces("[(])") == False
assert valid_braces("[({})](]") == False
