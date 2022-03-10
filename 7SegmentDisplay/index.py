def sevenSegments(S, N):
        # code here 
        charArr = list(S)
        # 7 segment digit with count of digits
        seg = [ 6 , 2 , 5 , 5 , 4 , 5 , 6 , 3 , 7 , 5 ]

        upper = 7 * N # upper bound
        lower = 2 * N # lower bound

        count_seg = sum(seg[int(charArr[i])] for i in range(N))

        min_list = [0, 1 , 2 , 4 , 5 , 7, 8]

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

                # print(ans , rem, lower, upper )
            

        print(ans)
        
        return ans


seg = sevenSegments('234567', 6)
print(seg)

