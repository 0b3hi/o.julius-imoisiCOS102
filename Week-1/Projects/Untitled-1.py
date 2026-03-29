def is_clean_palindrome(phrase):
    phrase_revered = phrase[:: -1]
    return phrase_revered == phrase


print(is_clean_palindrome("A man"))