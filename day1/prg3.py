class queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else: 
            self.__rear+=1
            self.__elements[self.__rear] =data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index],end=",")

    def get_max_size(self):
        return self.__max_size
    


def merge_queue(queue1,queue2):
    list1=[]
    list2=[]
    list3=[]
    
    while (not queue1.is_empty()):
        list1.append(queue1.dequeue())
    
    while (not queue2.is_empty()):
        list2.append(queue2.dequeue())
    
    check=0    
    if len(list1)<len(list2):
        length=len(list1)    
    else:
        length=len(list2)
        check=1
    
    if str(list1[0]).isdigit():
        integer=list1
        string=list2
    else:
        integer=list2
        string=list1
    flag=0
    j,k=0,0
    for i in range(0,2*length):
        if flag==0:
            list3.append(integer[j])
            flag=1
            j+=1
        elif flag==1:
            list3.append(string[k])
            flag=0
            k+=1
    if check==0:
        for i in list2:
            if i not in list3:
                list3.append(i)
    elif check==1:
        for i in list1:
            if i not in list3:
                list3.append(i)
    
    merged_queue=queue(len(list3))
    for item in list3:
        merged_queue.enqueue(item)
    return merged_queue


queue1=queue(3) 
queue2=queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
