arr = [0,2,7,8,10,13,15]

def binary_search(a, e, start, end):
    mid = (start+end)//2

    if start>end:

        return False
    else:

        if arr[mid]==e:
            return True
        elif arr[mid] > e:
            return binary_search(a,e,start,mid-1)
        elif arr[mid] < e:
            return binary_search(a,e,mid+1,end)
   
x= binary_search(arr,100,0,len(arr)-1)
print(x)