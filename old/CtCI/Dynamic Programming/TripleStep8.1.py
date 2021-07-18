def tripleStep(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return tripleStep(n-1)+tripleStep(n-2)+tripleStep(n-3)

def tripleStep_memoization(n):
    
    
if __name__=="__main__":
    # tripleStep_memoization(10)
    for i in range(5):
        print(f"{i}={tripleStep_memoization(i)}")