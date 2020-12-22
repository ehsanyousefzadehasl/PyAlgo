def insertion_sort(a):
    n = len(a)
    
    for j in range(1, n):
        key = a[j]
        
        i = j - 1
        
        while i > -1 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1 
            
        a[i + 1] = key
        
a = [1, 2, 0, -1, -2, 10, -10, 19, 234]
insertion_sort(a)

print(a)