'''
Input (stdin)
2
6
4 3 2 1 3 4
3
1 3 2

Output
Yes
No
'''

Empty_list = []
T = int(input())
for k in range(T):
    n = int(input())
    sl = list(map(int, input().split()))
    for p in range(n-1):
        if sl[0] >= sl[len(sl)-1]:
            a = sl[0]
            sl.pop(0)
        elif sl[0] < sl[len(sl)-1]:
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass
        if len(sl) == 1:
            Empty_list.append("Yes")
        if((sl[0] > a) or (sl[len(sl)-1] > a)):
            Empty_list.append("No")
            break
print("\n".join(Empty_list))
