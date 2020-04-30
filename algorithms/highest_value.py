def highest_value(arr):
    if arr == []:
        return 0
    return arr[0] if arr[0] > highest_value(arr[1:]) else highest_value(arr[1:])