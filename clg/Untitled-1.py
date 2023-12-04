def getMinMax(a, n):
    maxm = a[0]
    for i in range(1, n):
        if (a[i] > maxm):
            maxm = a[i]
        return a[i]
        
    minm = a[0]
    for j in range(1, n):
        if (a[j] < minm):
            minm = a[j]
        return a[j]
        
a = [3,2,1,56,1000,167]
n=6
res = getMinMax(a, n)
print(res)