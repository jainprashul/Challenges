# n number of digits
# s string of digits
# 7 segments digit 
#  a b c d e f g
#  

#User function Template for python3

class Solution:
    def sevenSegments(self, S, N):

        charArr = list(S)
        # 7 segment digit with count of digits
        seg = [ 6 , 2 , 5 , 5 , 4 , 5 , 6 , 3 , 7 , 5 ]

        upper = 2 * N # upper bound
        lower = 7 * N # lower bound

        count_seg = sum(seg[int(charArr[i])] for i in range(N))

        count_zeros = int(count_seg / 6)
        remaining_seg = count_seg % 6

        new_str = '0' * count_zeros 

        min_list = [0,  1 , 2 , 4 , 5 , 7, 8]

        c = 0 # counter

        # for _ in range(N):
            
        #     if (remaining_seg % seg[min_list[c]] == 0):
        #         if remaining_seg == 0:
        #             break
        #         new_str += str(min_list[c])
        #         remaining_seg -= seg[min_list[c]]
        #         # print(remaining_seg)
        #     else:
        #         c+=1

        ans = ''

        for i in range(N):
            lower -= 2
            upper -= 7
            for i in min_list:
                # reducing count by segment value
                rem = count_seg - seg[i]
                if rem >= lower and rem <= upper:
                    ans += str(i)
                    count_seg = rem
                    break

        # print(new_str)
        return ans
        # code here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        ob = Solution()
        print(ob.sevenSegments(S,N))
# } Driver Code Ends





    



