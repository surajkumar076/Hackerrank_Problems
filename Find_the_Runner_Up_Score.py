'''''
Input
5
2 3 6 6 5
Output
5

Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''''

if __name__ == '__main__':
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))

print (max(lis))
