def mergeSort(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1


arr = [55,22,65,24,76,223,7,2,75,213,8]
mergeSort(arr)
print(arr)
