# https://www.codechef.com/MARCH222D/problems/MISS_NUM/


def missingNumber(a, b , c ,d):
    l = [a, b, c, d]
    l.sort()

    return l

    #  -ve val will be x-y 
    #  min val will x/y floor value
    #  max val will x*y 
    #  mid val will x+y

t = int(input())
while t:
    t -= 1
    a, b, c, d = map(int, input().split(' '))

    print(missingNumber(a, b, c, d))




    