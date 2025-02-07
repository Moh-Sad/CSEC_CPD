"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

num = int(input())
items = list(map(int, input().split()))
s = 0
d = 0
for i in range(num):
    if i % 2 == 0:
        if items[0] > items[-1]:
            s += items[0]
            items.pop(0)
        else:
            s += items[-1]
            items.pop(-1)
    else:
        if items[0] > items[-1]:
            d += items[0]
            items.pop(0)
        else:
            d += items[-1]
            items.pop(-1)
print(s, d)
