'''
def reward_children(child_ids, chocolates, child_id, extra_chocolates):
    if extra_chocolates < 1:
        print("extra chocolates is less than 1")
        return
    if child_id not in child_ids:
        print("child id is invalid")
        return
    index = child_ids.index(child_id)
    chocolates[index] += extra_chocolates
    print(chocolates)
    total_chocolates = sum(chocolates)

    return total_chocolates
    '''
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    total_chocolates = sum(chocolates_received)
    return total_chocolates

def reward_child(child_id_rewarded, extra_chocolates):
    try:
        index = child_id.index(child_id_rewarded)
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
            return
        chocolates_received[index] += extra_chocolates
        print(chocolates_received)
    except ValueError:
        print("Child id is invalid")
total_chocolates = calculate_total_chocolates()
print(total_chocolates) # Output: 30
