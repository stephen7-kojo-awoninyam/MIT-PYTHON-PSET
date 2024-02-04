import numpy
# binary search
card = numpy.array([1,2,3,4,5,6])
query = 5

def locate_card(card,query):
    lo = 0
    hi = len(card)-1

    while lo <= hi:
       
        mid = (lo + hi)//2

        mid_num = card[mid]

        if mid_num == query:
            return mid
        elif mid_num < query:
            lo = mid + 1
        elif mid_num > query:
            hi = mid - 1
    return -1        



print(locate_card(card,query))