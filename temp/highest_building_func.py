def skyline(*args):
    temp=0
    for h in args:
        if h>temp:
            temp=h
    return temp

heights= input()
heights_list = list(map(int, heights.split()))

print(skyline(*heights_list))