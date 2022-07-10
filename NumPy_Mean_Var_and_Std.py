'''
Input
2 2
1 2
3 4

Output
[1.5 3.5]
[1. 1.]
1.11803398875

'''

import numpy as np

n,m= list(map(int, input().split()))
a= np.array([list(map(int, input().split())) for i in range(n)])
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a, axis=None), 11))
