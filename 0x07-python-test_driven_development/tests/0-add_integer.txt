Import `add_integer`

>>> add_integer = __import__('0-add_integer').add_integer

>>> add_integer(4, 5)
9

>>> add_integer(4, -5)
-1

>>> add_integer(4)
102

>>> add_integer('a')
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(2, 'b')
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(1, '2')
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(float('nan'))
Traceback (most recent call last):
ValueError: cannot convert float NaN to integer

>>> add_integer(1.55)
99

>>> add_integer(2 ** 10000* .1)
Traceback (most recent call last):
OverflowError: int too large to convert to float

>>> add_integer(float('inf'))
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer
