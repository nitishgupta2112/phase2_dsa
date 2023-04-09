class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def getgender(self):
        return self.gender
    def getname(self):
        return self.name
    def getage(self):
        return self.age
class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.qu=[None]*self.maxsize
        self.front=0
        self.rear=-1
    def isempty(self):
        if(self.front>self.rear):
            return True
        else:
            return False
    def isfull(self):
        if(self.rear==self.maxsize-1):
            return True
        return False
    def enqueue(self,data):
        if(self.isfull()):
            print("queue is full")
        else:
            self.rear+=1
            self.qu[self.rear]=data
            # print(data,"is added")
def dequeue(self):
        if(self.isempty()):
            print("queue is empty")
        else:
            val=self.qu[self.front]
            self.front+=1
            return val
        
def get_max(self):
    return self.maxsize
def display(self):
    for i in range(self.front,self.rear+1):
        print(self.qu[i],end=" ")
p1=person("Sri",20,"male")
p2=person("Arjun",22,"male")
p3=person("Krish",10,"female")
p4=person("Ramya",17,"female")
p5=person("sriyan",69,"male")

q1=queue(5)
q1.enqueue(p1)
q1.enqueue(p2)
q1.enqueue(p3)
q1.enqueue(p4)
q1.enqueue(p5)

str=input("Enter gender: ")
str=str.lower()

for i in range(q1.front,q1.rear+1):
    if(q1.qu[i].getgender()==str):
        print(q1.qu[i].getname()," ",q1.qu[i].getage()," ",q1.qu[i].getgender())
        print()