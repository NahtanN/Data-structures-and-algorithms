def counter(arr):
    if arr == []:
        return 0
    return 1 + counter(arr[1:])