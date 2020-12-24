def binary_search(a, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return binary_search(a, key, low, mid - 1)
        else:
            return binary_search(a, key, mid + 1, high)
    
    return -1

a = [1, 2, 3, 12, 16, 19, 39, 89, 99, 129, 139]

key = 139

print(binary_search(a, key, 0, len(a) - 1))

key = 100

print(binary_search(a, key, 0, len(a) - 1))