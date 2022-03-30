# https://www.codechef.com/MARCH222D/problems/CHEFRACES

def ChefRace(x,y, a,b):
    chef = [x, y]
    nonwin = [a, b]
    res = 0
    for i in chef: 
        if i  not in nonwin:
            res += 1
    return res

        


t = int(input())

while t:
    t -= 1
    x, y, a, b = map(int, input().split())
    print(ChefRace(x,y, a,b))
