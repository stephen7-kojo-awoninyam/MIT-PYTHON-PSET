import numpy
# binary search
card = numpy.array([1,2,3,4,5,6])
query = 5

def test_location(card,query,mid):
    mid_num = card[mid]
    if mid_num == query:
        if mid-1 >= 0 and card[mid-1]==query:
            return "left"
        else:
            return "found"
    elif mid_num < query:
        return "left"
    else:
        return "right"    

def locate_card(card,query):
    lo = 0
    hi = len(card)-1
    while lo <= hi:
        mid = (lo + hi)//2
        
        results = test_location(card,query,mid)
        if results == "found":
            return mid
        elif results == "right":
            lo = mid + 1
        elif results == "left":
            hi = mid - 1
    return -1        



print(locate_card(card,query))