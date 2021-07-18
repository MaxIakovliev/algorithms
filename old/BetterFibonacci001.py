def better_fibonacci(n):
    if n==0 or n==1:
        return n
    rng=[0,1]
    while len(rng)<=n:
        rng.append(rng[-1]+rng[-2])
    return rng[n]
   

print("expected:2, actual "+str(better_fibonacci(3)))
print("expected:55, actual "+str(better_fibonacci(10)))
    