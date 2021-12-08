arrivals=['one','two','three','four','five','six','seven']
def party_late(arrivals,name):
    if len(arrivals) % 2!= 0:
        late_list = [late for late in arrivals if late in arrivals[(len(arrivals)//2)+1:]]
    else:
        late_list = [late for late in arrivals if late in arrivals[(len(arrivals)//2:]]
    late_list.pop()
    return name in late_list
    