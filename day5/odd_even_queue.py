class queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.elements = [None] * self.max_size
        self.rear = -1
        self.front = 0

    def is_empty(self):
        if(self.front>self.rear):
            return True
        return False
    
    def is_full(self):
        if(self.rear==self.max_size-1):
            return True
        return False 
    
    def enqueue(self,data):
        self.rear+=1
        self.elements[self.rear]=data
    
    def dequeue(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self.front+=1

    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.elements[index],end=" ")
        print()

que = queue(7)
que.enqueue(2)
que.enqueue(7)
que.enqueue(9)
que.enqueue(4)
que.enqueue(6)
que.enqueue(5)
que.enqueue(10)
a = queue(7)
b = queue(7)
for i in range(que.front,que.rear+1):
    if que.elements[i]%2==0:
        a.enqueue(que.elements[i])
print("The even are")
a.display()
for i in range(que.front,que.rear+1):
    if que.elements[i]%2!=0:
        b.enqueue(que.elements[i])
print("The odd are")
b.display()

