>>> MyList = __import__('1-my_list').MyList

>>> new_list = MyList()

>>> new_list
[]

>>> new_list.print_sorted()
[]

>>> new_list.append(4)

>>> new_list
[4]

>>> new_list.append(2)

>>> new_list
[4, 2]

>>> new_list.append(-1)

>>> new_list
[4, 2, -1]

>>> new_list.print_sorted()
[-1, 2, 4]

>>> new_list
[4, 2, -1]
