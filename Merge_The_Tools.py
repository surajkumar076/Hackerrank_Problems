''''
Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Output

AB
CA
AD

''''

def merge_the_tools(string, k):
    # your code goes here
    while string:
        s= string[:k]
        seen=''
        for i in s:
            if i not in seen:
                seen += i
        print(seen)
        string= string[k:]
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
