def binary_search(list1, n,low,high):  
    while low <= high:  
        mid = low+(high - low) // 2 
        if list1[mid] < n:  
            low = mid + 1    
        elif list1[mid] > n:  
            high = mid - 1  
        else:  
            return mid  
    return -1  

array = list(map(int,input().split(",")))
n = int(input())
result = binary_search(array, n,0,len(array)) 
if result != -1:  
    print(array.index(n))  
else:  
    print(-1) 