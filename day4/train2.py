class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        temp=self.headval
        while temp is not None:
            print(temp.data.comp_name,temp.data.t_seat,temp.data.n_pass)
            print()
            temp=temp.next

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
            while(temp.next != None):
                temp=temp.next
            temp.next=newnode

    def len(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)

class train:
    def __init__(self,tname,c_list):
        self.tname=tname
        self.c_list=c_list

    def get_train_name(self):
        return self.tname
    
    def get_compartment(self):
        self.c_list.listprint()

    def count_compartment(self):
        self.c_list.len()
    
    def check_vacancy(self):
        temp=self.c_list.headval
        cnt=0
        while temp is not None:
            if(temp.data.t_seat-temp.data.n_pass >= temp.data.t_seat//2):
                cnt+=1
            temp=temp.next
        print(cnt)


class Compartment:
    def __init__(self,comp_name,n_pass,t_seat):
        self.comp_name=comp_name
        self.t_seat=t_seat
        self.n_pass=n_pass
    
list=linkedlist()
c1=Compartment("SL",250,400)
c2=Compartment("2AC",125,280)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,210)
list.atend(c1)
list.atend(c2)
list.atend(c3)
list.atend(c4)
list.atend(c5)

t1=train("Rajadhani",list)
t1.count_compartment()
t1.check_vacancy()
#t1.get_compartment()
print(t1.get_train_name())