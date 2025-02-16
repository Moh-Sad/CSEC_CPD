"""
    Author: Mohammed Sadik
    Language: Python 3
    Difficulty: Easy
    Platform: Codeforces
"""

n, k = map(int, input().split())
items =list(map(int, input().split()))
check = items[k - 1]
count = 0
     
for i in range(n):
    if items[i] >= check and items[i] != 0:
        count += 1
            
print(count)
