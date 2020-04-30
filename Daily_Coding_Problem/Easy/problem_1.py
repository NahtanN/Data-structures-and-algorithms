#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def add_up(arr, k):
    try:
        return True if k - arr[0] in arr else add_up(arr[1:], k)
    except IndexError:
        return False



