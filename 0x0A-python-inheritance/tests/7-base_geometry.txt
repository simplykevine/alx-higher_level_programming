>>> BaseGeo = __import__('7-base_geometry').BaseGeometry

>>> base = BaseGeo()

>>> base.area()
Traceback (most recent call last):
Exception: area() is not implemented

>>> base.integer_validator()
Traceback (most recent call last):
TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

>>> base.integer_validator("age")
Traceback (most recent call last):
TypeError: integer_validator() missing 1 required positional argument: 'value'

>>> base.integer_validator("age", (4,))
Traceback (most recent call last):
TypeError: age must be an integer

>>> base.integer_validator("my_int", 12)

>>> base.integer_validator("width", 89)

>>> base.integer_validator("name", "John")
Traceback (most recent call last):
TypeError: name must be an integer

>>> base.integer_validator("age", 0)
Traceback (most recent call last):
ValueError: age must be greater than 0

>>> base.integer_validator("distance", -4)
Traceback (most recent call last):
ValueError: distance must be greater than 0

>>> base.integer_validator("age", [3])
Traceback (most recent call last):
TypeError: age must be an integer

>>> base.integer_validator("age", True)
Traceback (most recent call last):
TypeError: age must be an integer

>>> base.integer_validator("age", {3, 4})
Traceback (most recent call last):
TypeError: age must be an integer

>>> base.integer_validator("age", None)
Traceback (most recent call last):
TypeError: age must be an integer
