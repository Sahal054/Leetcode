
def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start + 1, end - 1)






arr = [5, 4, 3, 2, 1]
n = len(arr)
reverseArray(arr, 0, n - 1)
print(arr)
