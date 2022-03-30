# https://www.codechef.com/START32D/problems/FINDSHOES

# n friends
# m left shoes 
# find the number of pairs of shoes that can be bought

def findShoes(n, m):
    count = 0
    if (m >= n):
        count = n
    elif (m < n):
        x = n - m
        count = (2 * x) + m
    
    return count


t = int(input())
while(t):
    n, m = map(int, input().split())
    print(findShoes(n, m))
    t -= 1

