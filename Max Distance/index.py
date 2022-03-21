# https://practice.geeksforgeeks.org/contest/interview-series-microsoft-4413/problems/

# arr A of len N 
#  A and B have condition =
# only move if next index val is >= current index val
# find the max distance between two index in A and B
#  both should go in opposite dir for max len

def Maxdistance(arr, n):
    max_dist = 0
    ptr_left = 0
    ptr_right = 0
    movedRight = False

    while(ptr_right < n):
        # only move if next index val is >= current index val
        if (arr[ptr_right + 1] >= arr[ptr_right] and ptr_right + 1 < n):
            # move ptr to right
            ptr_right += 1
            movedRight = True
        elif (ptr_left > 0 and arr[ptr_left - 1] >= arr[ptr_left]):
            # move ptr to left
            ptr_left -= 1
        else:
             # update max_dist
            max_dist = max(max_dist, ptr_right - ptr_left)
            # move both ptrs to next index
            ptr_right += 1
            if (movedRight) : 
                ptr_left = ptr_right

       
    
    return max_dist





    

