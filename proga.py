import random

arr = [random.randint(2, 99) for i in range(30)]
max_len = 0
markers = []
for elem in arr:
    krat_arr = []
    for i in range(2, 10):
        if elem % i == 0:
            krat_arr.append(i)
    markers.append(krat_arr)
    if len(krat_arr) > max_len:
        max_len = len(krat_arr)

most_multiple_numbers = []
i = 0
while i < len(markers):
    if len(markers[i]) == max_len:
        most_multiple_numbers.append(i)
    i += 1

print('сам массив:', arr)
for i in set(most_multiple_numbers):
    print('число:', arr[i])
    print('числа, которым оно кратно:', markers[i])
    print()
