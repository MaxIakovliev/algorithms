def binary_search(a_list, item):
    left=0
    right=len(a_list)-1
    mid=(int)((left+right)/2)
    
    while True:
        if a_list[mid]==item or a_list[left]==item or a_list[right]==item:
            return True
        if mid==0 or mid== len(a_list) or (right==len(a_list)-1 and right-left==1) or (left==0 and right-left==1):
            return False

        elif item<a_list[mid]:
            right=mid
            mid=(int)((left+right)/2)
        elif item>a_list[mid]:
            left=mid
            mid=(int)((left+right)/2)



def bin_search2(a,item):
    left=0
    right=len(a)-1
    mid= (int)((left+right)/2)
    return helper(a,left,mid,item) or helper(a,mid, right,item)

def helper(a,left, right, item):
    if a[left]==item or a[right]==item:
        return True
    if right-left<=1:
        return False
    if item<a[right]:
        mid= (int)((left+right)/2)
        return helper(a,left,mid,item) or helper(a,mid, right,item)
    if item>a[right]:
        mid= (int)((right+ len(a)-1)/2)
        left=right
        right=len(a)-1
        return helper(a,left,mid,item) or helper(a,mid, right,item)
        
    
if __name__=="__main__":
    # a=[-1,2,3,4,5,6,7,8,9,10]
    a=[-8, -2, -1, 0]
    for i in range(-9,12):
        print("i={0}; res={1}".format(str(i),str(bin_search2(a,i))))