'''
def bob(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = list(map(int,input().split(", ")))
bob(arr)
print(*arr,sep=", ")

-----------------------------------------------------------
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = list(map(int,input().split(", ")))
size = len(data)
selectionSort(data, size)
print(*data,sep=", ")

---------------------------------------------------------------
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
data = list(map(int,input().split(", ")))
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(*data,sep=", ")

----------------------------------------------------------------------
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
data = list(map(int,input().split(", ")))
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(*data,sep=", ")
----------------------------------------------------------------------
9 not done
-----------------------------------------------------------------------
def reverse_stack(stack):
    if len(stack) == 0:
        return stack
    
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)
    return stack
    
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)
my_stack = list(map(int,input().split(" ")))
reverse_stack(my_stack)
print(*my_stack, sep=" ") 
---------------------------------------------------------------------------
def reverse_second_half(stack):
    if len(stack) % 2 == 0:
        mid = len(stack) // 2
    else:
        mid = len(stack) // 2 + 1
    temp_stack = []
    for i in range(mid, len(stack)):
        temp_stack.append(stack[i])
    for i in range(mid, len(stack)):
        stack.pop()
    for i in range(len(temp_stack)):
        stack.append(temp_stack.pop())
    return stack
stack = list(map(int,input().split(" ")))
reverse_second_half(stack)
print(*stack,sep=" ")
----------------------------------------------------------------------------------
'''