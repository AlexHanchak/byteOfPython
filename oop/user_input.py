def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


forbidden = ('!', '?', '.', ':', ';', '-', '--', '()', '[]', '...', '`', '""', '/', ',', ' ')


something = input('input text: ').lower().replace(" ", "")

# 36 / 3

if (is_palindrome(something)):
    print('yas, it`s palindrome')
else:
    print('no, is not')


