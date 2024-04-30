def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]


def brute_force_cow_transport(cows,limit=10):
    cows = cows.copy()
    brutetrips = []
    trips = []
    num = 0

    names = list(cows.keys())

    for partition in get_partitions(names):
        for name in partition:
            for cow in name:
                num += cows[cow]
                if num <= 10:
                    trips.append(cow)
                else:
                    continue 
            num = 0
            if trips not in brutetrips:
                brutetrips.append(trips) 
            trips = []      
    return brutetrips        

  

cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}

print(brute_force_cow_transport(cows))