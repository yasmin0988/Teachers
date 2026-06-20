def sum_numbers(*args):
    sum=0
    for num in args:
        sum += num
    return sum

nums = input()

if nums == "":
    print(0)
else:
    number_list=[]
    numbers = nums.split()

    for n in numbers:
        number_list.append(int(n))

print(sum_numbers(*number_list))