arr = [3,5,0,2,1,4]

def bubbleSort(a):

    n = len(a)

    if n <=1:
        return a
    else:
        for i in range(0,n-1):
         for j in range(i+1,n):
            if a[i] > a[j]:
               a[i],a[j] = a[j], a[i]
        return a
    
print(bubbleSort(arr))
