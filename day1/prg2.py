class node:
    def _init_(self,data=None):
        self.data=data
        self.next=None
class slinkedlist:
    def _init_(self):
        self.headval=None
    def listprint(self):
        printval=self.headval  #temp
        while printval is not None:
            print(printval.data,end=" ")
            printval=printval.next
    def athead(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            newnode.next=self.headval
            self.headval=newnode
    def atend(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def atposition(self,data,pos):
        newnode=node(data)
        cnt=1
        if(pos==1):
            self.athead(data)
        else:
            temp=self.headval
            while(cnt<pos-1):
                temp=temp.next
                cnt+=1
            if(temp.next==None):
                self.atend(data)
            
            newnode.next=temp.next
            temp.next=newnode
            

list=slinkedlist()
list.atend('A')
list.atend('n')
list.atend('*')
list.atend('/')
list.atend('a')
list.atend('p')
list.atend('p')
list.atend('l')
list.atend('e')
list.atend('*')
list.atend('a')
list.atend('/')
list.atend('day')
list.atend('*')
list.atend('/')
list.atend('k')
list.atend('e')
list.atend('e')
list.atend('p')
list.atend('s')
list.atend('/')
list.atend('*')
list.atend('a')
list.atend('/')
list.atend('*')
list.atend('d')
list.atend('o')
list.atend('c')
list.atend('t')
list.atend('o')
list.atend('r')
list.atend('*')
list.atend('A')
list.atend('w')
list.atend('a')
list.atend('y')
list.listprint()
print()
s=''
temp=list.headval
while temp is not None:
    if(temp.data=='*' or temp.data=='/'):
        if(temp.next.data=='/' or temp.next.data=='*'):
            s+=' '
            temp=temp.next.next
            s+=temp.data.upper()
            temp=temp.next
            
        else:
            temp.data=' '
            s+=temp.data
            temp=temp.next
    else:
        s+=temp.data
        temp=temp.next
print(s)