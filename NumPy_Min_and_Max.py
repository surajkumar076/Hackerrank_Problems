'''
Input
4 2
2 5
3 7
1 3
4 0

Output
3
'''

import numpy

n,m=map(int,input().split())
list=[list(map(int,input().split())) for i in range(n)]
ar=numpy.array(list)
print(max(numpy.min(ar,axis=1)))
