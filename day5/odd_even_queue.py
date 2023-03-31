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
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size

que = queue(5)
print("Queue is full",que.is_full())
print("is empty",que.is_empty())
que.enqueue(100)
que.enqueue(200)
que.enqueue(300)
que.enqueue(400)
que.enqueue(500)
que.display()
