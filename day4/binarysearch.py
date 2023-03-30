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

list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45 
result = binary_search(list1, n,0,len(list1)) 
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1") 