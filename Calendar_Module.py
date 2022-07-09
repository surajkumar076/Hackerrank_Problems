'''
Input
08 05 2015

Output
WEDNESDAY
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

d,m,y= map(int,input().split())
print((calendar.day_name[calendar.weekday(y,d,m)]).upper())
