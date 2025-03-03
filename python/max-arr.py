def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 5, 7, 2, 8]))
