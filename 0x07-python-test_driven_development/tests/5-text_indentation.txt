>>> text_indentation = __import__('5-text_indentation').text_indentation

>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'

>>> text_indentation("Holberton. School? How are you: John")
Holberton.
<BLANKLINE>
School?
<BLANKLINE>
How are you:
<BLANKLINE>
John

>>> text_indentation(2)
Traceback (most recent call last):
TypeError: text must be a string

>>> text_indentation("Aptech. School")
Aptech.
<BLANKLINE>
School
