class node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval =None

class slinkedlist:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
      NewNode = node(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode

    def AtEnd(self, newdata):
      NewNode = node(newdata)
      if self.headval is None:
        self.headval = NewNode
        return
      laste = self.headval
      while(laste.nextval):
        laste = laste.nextval
      laste.nextval=NewNode
    
    def Inbetween(self,middle_node,newdata):
      if middle_node is None:
        print("The mentioned node is absent")
        return
      NewNode = node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode

list = slinkedlist()
list.headval= node("mon")
e2 = node("tue")
e3 = node("wed")
list.headval.nextval =e2
e2.nextval = e3

list.AtBegining("Sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval,"Fri")

list.listprint()

