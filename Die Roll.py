"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

y, w = map(int, input().split())
max = max(y, w)
d = 6 - max + 1
n = 6
if d % 2 == 0:
    d = d // 2
    n = n // 2
if d % 3 == 0:
    d = d // 3
    n = n // 3
print(str(d) + '/' + str(n))
