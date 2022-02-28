# from datetime import datetime
# def solve(c):
#     s = [x for x in range(0,c+1)]

#     for i in s:
#         for j in range(i, len(s)+1):
#             temp = (i**2 + j**2)
#             if temp == c:
#                 return True
#     return False
from math import sqrt
def optimal(c):
    left = 0
    right = int(sqrt(c))
    while left <= right:
        curr = left**2 + right **2
        if curr == c:
            return True
        elif left <= curr:
            left = curr + 1
        else:
            right = curr -1
    return False

def main():
    #start = datetime.now()
    nums = [5,6,7]
    #res = map(solve(7), nums)
    res = optimal(5)
    print(res)
    #end = datetime.now()
    #print(end-start)

main()
