# The Rating Dilemma
# https://www.codechef.com/MARCH222D/problems/RATING

#  x +ve 
#  y -ve
#  S = x + y
#  find max x*y

#  s = 5
#  [-1,6] {-2, 7} {-3, 8} {-4, 9} {-5, 10}

# s = 6
# [-1, 7} {-2, 8} {-3, 9} {-4, 10} {-5, 11} {-6, 12}

def maxProduct(sum):

    if sum == 0:
        return -1
    return -(sum + 1)

t = int(input())
while t:
    t -= 1
    s = int(input())
    print(maxProduct(s))