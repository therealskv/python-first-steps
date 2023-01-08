def reverse_slice(arr, start, end):
    return arr[0:start][::-1][0:end]


arr = [0, 1, 2, 3, 4, 5]
print(reverse_slice(arr, 4, 3))