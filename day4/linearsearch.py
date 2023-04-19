def linearSearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1
array = list(map(int,input().split(",")))
x = int(input())
n = len(array)
result = linearSearch(array,n,x)
if result == -1:
    print(-1)
else:
    print(array.index(x))