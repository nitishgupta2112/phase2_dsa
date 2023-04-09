
import operator

ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2] == destination):
            count+=1
    return count
def find_passengers_per_flight():
    count=0
    flight=[]
    number_of_pass = []
    for i in ticket_list:
        string_list=i.split(":")
        if string_list[0] in flight:
            index = flight.index(string_list[0])
            number_of_pass[index] +=1
        else:
            flight.append(string_list[0])
            number_of_pass.append(1)
    result_list = []
    for i, j in zip(flight, number_of_pass):
        result_list.append(str(i) + ":" + str(j))
        return result_list

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    list_passenger_per_flight = find_passengers_per_flight()
    dict1 = {}
    print(list_passenger_per_flight)
    for i in list_passenger_per_flight:
        string_list=i.split(":")
        dict1[string_list[0]] = int(string_list[1])
    dict2 = []
    for key, value in sorted(dict1.items(), key=lambda item: item[1], reverse = True):
        dict2.append(str(key)+":"+str(value))
    return dict2
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
find_passengers_per_flight()
print(sort_passenger_list())

#(prices.iteritems(), lambda x, y : cmp(x[1], y[1])