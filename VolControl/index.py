#  https://www.codechef.com/START32D/problems/VOLCONTROL
# cat input.txt | C:/Python310/python.exe index.py    

# X -> Y
# +1 -1
# find n steps to reach Y

def countSteps(x, y):
    return abs(x - y)


t = int(input())
while(t):
    x, y = map(int, input().split())
    print(countSteps(x, y))
    t -= 1
