def binarysearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5]
target = 3

result = binarysearch(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")