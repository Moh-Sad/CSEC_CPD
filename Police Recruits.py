"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

n = int(input())
case = list(map(int, input().split()))
untreated = 0
treat = 0
for i in range(n):
    if case[i] == -1:
        if treat > 0:
            treat -= 1
        else:
            untreated += 1
    else:
        treat += case[i]
print(untreated)
