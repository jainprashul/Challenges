# https://www.codechef.com/START32D/problems/BSCOST

# binary string of Length N 
# every occurrence of 01 in S, a tax of X rupees will be charged,
# every occurrence of 10 in S, a tax of Y rupees will be charged.
# can arranges str in any order




def binaryStringCost(n , x, y , str):

    x_count = str.count('1')
    y_count = str.count('0')
    cost = 0
    if (x_count == 0 or y_count == 0):
        return cost
    
    cost = min(x , y)

    return cost

t = int(input())
while(t):
    n, x, y = map(int, input().split())
    str = input()
    print(binaryStringCost(n, x, y, str))
    t -= 1
    