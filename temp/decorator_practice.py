import datetime


def running_time(f):
    def wrapper():
        before = datetime.datetime.now()
        f()
        after = datetime.datetime.now()
        print(after-before)
    return wrapper

def list_nums():
    n = int(input("Enter the last number on your list: "))
    i = 1
    for i in range(i, n):
        num_list = []
        num_list.append(i)
        i += 1
    print(num_list)
    return num_list

list_nums()
running_time(list_nums)