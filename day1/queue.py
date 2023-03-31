class queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return False
        return True
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return False
        return True
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else: 
            self.__elements[self.__rear]=data
            self.__rear+=1
            
    
    def display(self):
        for index in range(self.__front,self.__rear+1):
            if self.__elements[index]%2==0:
                print("odd Queue")
                print(self.__elements[index])
            else:
                print("even Queue")
                print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size

que = queue(10)
print("Queue is full",que.is_full())
print("is empty",que.is_empty())
que.enqueue(2)
que.enqueue(7)
que.enqueue(9)
que.enqueue(4)
que.enqueue(6)
que.enqueue(5)
que.enqueue(10)
que.display()
