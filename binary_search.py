# Binary Search O(log(n))
arr = list(range(10))


def bs(arr, val, start, end):
    mid = (start+end)//2

    if val == arr[start]:
        return start
    elif val == arr[end]:
        return end
    elif val == arr[mid]:
        return mid

    if len(arr) == 2 or val > arr[end] or val < arr[start]:
        return False

    if val > arr[mid]:
        return bs(arr, val, mid+1, end)
    else:
        return bs(arr, val, start, mid-1)


print(bs(arr, 10, 0, len(arr)-1))
