class stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def  is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size

stk = stack(4)
print("is stack empty",stk.is_empty)
stk.push(6)
stk.push(5)
stk.push(4)
stk.push(9)
stk.display()
print("size of stack is",stk.get_max_size())
print("Elemented deleted",stk.pop())
print("After deleting")
stk.display()
print("size",stk.get_max_size())
