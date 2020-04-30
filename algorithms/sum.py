def sum_total(arr):
    if arr == []:
        return 0
    return arr[0] + sum_total(arr[1:])
