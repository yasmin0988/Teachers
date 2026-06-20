def pick_evens(*args):
    even_list = []
    for num in args:
        if num%2 == 0:
            even_list.append(num)
    return even_list
        
nums = input()
nums_list = list(map(int, nums.split()))
print(pick_evens(*nums_list))

