def insertion_sort(a):
	for i in range(1,len(a)):
		val=a[i]
		j=i
		while j>0 and val<a[j-1]:
			a[j]=a[j-1]
			j=j-1
		a[j]=val
	return a
		
def insertion_sort_desc(a):
	for i in range(len(a)-1,-1,-1):
		val=a[i]		
		j=i
		while j<len(a)-1 and val<a[j+1]:
			a[j]=a[j+1]
			j=j+1
		a[j]=val
	return a
