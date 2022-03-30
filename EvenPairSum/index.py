#  https://www.codechef.com/problems/EVENPSUM

#  x , y
#  x <= A and y <= B
#  x + y = C
#  c % 2 = 0

#  x  even y even = even
#  x  even y odd  = odd
#  x  odd y even  = odd
#  x  odd y odd   = even

# a = 3 b = 5 // 15
# {1, 1} , {1, 2} , {1, 3} , {1, 4} , {1, 5}
# {2, 1} , {2, 2} , {2, 3} , {2, 4} , {2, 5}
# {3, 1} , {3, 2} , {3, 3} , {3, 4} , {3, 5}





# loop a =1  count= 2
# loop a =2  count= 3









# 11
# 1 3 5 7 9

# no of pairs = a * b

# co

def even_pair(a, b):
    total_pairs = a * b
    return int((total_pairs + 1) / 2)
    

 

    # # l = []
    # for x in range(1, a + 1):
    #     # if x is odd
    #     if x % 2 != 0: # odd
    #         count += 
    #         # count += no of odd in B 
    #     # if x is even
    #     #  count += no of even in B
    #     pass
    # return count




t = int(input())

while (t > 0):

    ip = input().split(' ')
    a = int(ip[0])
    b = int(ip[1])

    print(even_pair(a, b))

    t -= 1


