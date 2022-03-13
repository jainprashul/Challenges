#  n -arrr tree 
#  https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1
#  check if the tree is mirror image of each other or not
#  e - number of edges in the tree
#  A[] , B[] - array of edges
#  2* e separated by space
#  {1 , 2 , 1, 3} 1-2 1-3
#  {1 , 3 , 1 , 2} 1-3 1-2



def checkMirrorTree(n, e, A, B):
    # create a map of the tree
    # key - node value
    # value - list of children
    tree = {}
    for i in range(0,2*e, 2):
        if A[i] not in tree:
            tree[A[i]] = []
        else:
            tree[A[i]].append(B[i])
        if B[i] not in tree:
            tree[B[i]] = []
        tree[B[i]].append(A[i])


    print(qu)

    
        
   
    
n = 7
e = 7
A = map(int , '1 2 1 3 2 4 2 5 5 6 6 7 6 9'.split(' '))
B = map(int, '1 3 1 2 2 5 2 4 5 6 6 9 6 7')

chec = checkMirrorTree( 4, 2 , [1, 2, 1, 3], [1, 3, 1, 2] )
print(chec)