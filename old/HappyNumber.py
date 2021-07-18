def is_happy_number(num):
    if num >10:
        count=0
        while num!=1 and count!=10:
            sm=0
            divider=10
            while num>0:
                t=num %divider
                num=num -t
                num=(int)(num/10)
                sm+= (t*t)                
                divider=divider
            num=sm
            count+=1
        if num==1:
            return True
        else:
            return False
    else:
        return False
print(is_happy_number(10))
        