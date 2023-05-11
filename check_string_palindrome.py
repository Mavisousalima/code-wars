def is_palindrome(word):
    word = word.lower()
    word = word.replace(' ', '')

    return word == word[::-1]


assert is_palindrome('ana') == True
assert is_palindrome('level') == True
assert is_palindrome('house') == False
assert is_palindrome('Abba') == True
assert is_palindrome('WTObIAcwCyRaeeREEAryCWCaiBOtW') == True
assert is_palindrome('A luna ese anula') == True
