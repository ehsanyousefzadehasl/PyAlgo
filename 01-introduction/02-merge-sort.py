import time

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
        

def merge(a, p, q, r):
    L = []
    R = []
    
    for i in range(p, q + 1):
        L.append(a[i])
    L.append(1000000000)
    
    for j in range(q + 1, r + 1):
        R.append(a[j])
    R.append(1000000000)
    
    print(L, R)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

# For Quick Testing Purposes            
#a = [1, 2, 0, -1, -2, 10, -10, 19, 234, 10]
#merge_sort(a, 0, len(a) - 1)
#print(a)


# For testing how fast it is with more numbers to sort
n = 100000

a = []
f = open('input/input.in', 'r')


for i in range(n):
    a.append(int(next(f).split()[0]))

start_time = time.time()

merge_sort(a, 0, len(a) - 1)

end_time = time.time()

print(a)

print("Execution Time of Merge Sort: " + str(end_time - start_time))