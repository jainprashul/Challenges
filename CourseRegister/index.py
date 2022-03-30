# https://www.codechef.com/START32D/problems/COURSEREG

# n 
# max courses m
# k students already registered
# find if n students can register

def checkCourse(n, m, k):
    if m - k >= n:
        return "YES"
    return "NO"

T = int(input())
while(T):
    n, m, k = map(int, input().split())
    print(checkCourse(n, m, k))
    T -= 1

