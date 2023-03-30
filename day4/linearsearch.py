def linearSearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1
array = [1,2,3,4,5,6]
x = 7
n = len(array)
result = linearSearch(array,n,x)
if result == -1:
    print("element not found")
else:
    print("element found",result)