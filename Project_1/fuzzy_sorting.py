
import numpy as np
import random


def swap_list(A:list,id_1, id_2):
    dummy = A[id_1]
    A[id_1]=A[id_2]
    A[id_2]=dummy
    return A

def find_intersection(A,p,r):
    rand_ = np.random.randint(p,r)
    A = swap_list(A,rand_,r)
    a = A[r][0]
    b = A[r][1]

    for i in range(p,r):
        if A[i][0]<=b and A[i][1]>=a:
            if A[i][0]>a:
                a = A[i][0]
            if A[i][1]<b:
                b = A[i][1]
    return a,b 

def partition_right(A, a, p, r):
    i = p-1
    for j in range(p,r):
        if A[j][0]<a:
            i=i+1
            swap_list(A,i,j)
    swap_list(A,i+1,r)
    return i+1

def partition_left(A,b,p,t):
    i = p-1
    for j in range(p,t):
        if A[j][1]<b:
            i=i+1
            swap_list(A,i,j)
    swap_list(A,i+1,t)
    return i+1

def fuzzy_sort(A,p,r):
    if p<r:
        a,b = find_intersection(A,p,r)
        t = partition_right(A,a,p,r)
        q = partition_left(A,b,p,t)
        fuzzy_sort(A,p,q-1)
        fuzzy_sort(A,t+1,r)

    return A


if __name__=="__main__":

  
    input_arr = [[5.078780, 5.078993], [7.633073, 7.633180], [2.919274, 2.919369], [3.410284, 3.410314], [5.769048, 5.769161], [0.904946, 0.905058]]
    print(fuzzy_sort(input_arr,0,len(input_arr)-1))
