'''
Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Output
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''

numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
