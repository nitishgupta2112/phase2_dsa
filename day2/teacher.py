def update_mark_list(mark_list,new_element,pos):
    mark_list.append(0)
    l=len(mark_list)-1
    for i in range(len(mark_list)-pos-1):
        mark_list[l],mark_list[l-1]=mark_list[l-1],mark_list[l]
        l-=1
    mark_list[pos]=new_element
    return mark_list

def find_marks(mark_list,pos1,pos2):
    lst=[]
    lst.append(mark_list[pos1])
    lst.append(mark_list[pos2])
    return lst

mark_list = [89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list,new_element,pos))
print(find_marks(mark_list,pos1,pos2))