def mergesort(arr):
    if len(arr) > 1:
        lenarr = len(arr)
        mid = lenarr//2

        L = arr[0:mid]
        R = arr[mid:lenarr]

        mergesort(L)
        mergesort(R)

        #merge them back together
        i = 0
        j = 0
        k = 0
        while (i < len(L)) and (j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

    print(arr)
    
    return arr
    
arr = [2, 5, 3, 6, 8, 11]   
print(mergesort(arr)) 




