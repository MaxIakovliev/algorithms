def mergeSort(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
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


def mergeSortDesc(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i= len(left)-1
        j=len(right)-1
        k=len(left)-1
        while i >=0 and j >=0:
            if left[i] < right[j]:
                arr[k]=left[i]
                i=i-1
            else:
                arr[k]=right[j]
                j=j-1
            k=k-1
		
        print(left)
		
        i= len(left)-1
        j=len(right)-1
        k=len(left)-1
			
        while i >=0:            
            arr[k]=left[i]
            i=i-1
            k=k-1

        i= len(left)-1
        j=len(right)-1
        k=len(left)-1

        while j >=0:
            arr[k]=right[j]
            j=j-1
            k=k-1		
			

arr = [55,22,65,24,76,223,7,2,75,213]
mergeSortDesc(arr)
print(arr)
