#  https://www.codechef.com/START32D/problems/MAXTHEMIN

# array A of size  N
# atmost k operations
# A[i] = A[i+1] ; 1 <= i <= N-1
# A[i] = A[i-1] ; 2 <= i <= N

def maxTheMin(n, k, arr):
    max_val = 0

    print('case ',arr)

    for i in range(1 , n):
        if k > n:
            break

        if i == 0:
            max_val = max(max_val, arr[i] , arr[i+1])
        elif i == n-1:
            max_val = max(max_val, arr[i] , arr[i-1])
        else:
            max_val = max(max_val, arr[i], arr[i+1] , arr[i-1])

        arr[i] = max_val
        print(arr)



    return min(arr)


t = int(input())
while(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxTheMin(n, k, arr))
    t -= 1





