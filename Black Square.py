"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

a = list(map(int, input().split(' ')))
pattern = list(input())
calories = 0
for i in pattern:
    calories += a[int(i) - 1]
print(calories)
