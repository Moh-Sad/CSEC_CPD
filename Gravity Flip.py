"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

n = int(input())
items = list(map(int, input().split()))
items.sort()
for i in range(n):
    print(items[i], end=" ")
