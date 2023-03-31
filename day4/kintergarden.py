text=input().split(" ")
vocabulary=['sun','in','east','doctor','day']
dic=[]
for i in text:
    if i not in vocabulary:
        dic.append(i)
dic1=set(dic)
print(dic1)