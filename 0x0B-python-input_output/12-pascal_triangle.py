#!/usr/bin/python3
'''Pascal triangle of n:'''


def pascal_triangle(n):
    '''returns the pascals triangle '''
    outer_list = []

    for i in range(n):
        if i == 0:
            outer_list.append([1])
        elif i == 1:
            outer_list.append([1, 1])
        else:
            last_list = outer_list[-1]
            count = 0
            new_list = [1]
            while count < len(last_list):
                try:
                    new_list.append(last_list[count] + last_list[count + 1])
                    count += 1
                except IndexError:
                    break
            new_list.append(1)
            outer_list.append(new_list)
    return outer_list
