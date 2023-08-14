import time

def insertion_sort(a):
    n = len(a)
    
    for j in range(1, n):
        key = a[j]
        
        i = j - 1
        
        while i > -1 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1 
            
        a[i + 1] = key

# For Quick Testing purpose        
#a = [1, 2, 0, -1, -2, 10, -10, 19, 234]
#insertion_sort(a)
#
#print(a)


# For testing how fast it is with more numbers to sort
n = 10000

a = []
f = open('input/input.in', 'r')


for i in range(n):
    a.append(int(next(f).split()[0]))

start_time = time.time()

insertion_sort(a)

end_time = time.time()

print(a)

print("Execution Time of Insertion Sort: " + str(end_time - start_time))