list1=['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
list2.reverse()
list3=[]
for i in range(0,len(list1)):
    if list2[i]!=None:
        list3.append(list1[i]+list2[i])
    else:
        list2[i] = ''
        list3.append(list1[i]+list2[i])
print(*list3)