#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for item in dir(hidden_4):
        if item[0:2] != "__":
            print("{:s}".format(item))
