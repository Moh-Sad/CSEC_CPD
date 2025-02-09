"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

k, r = map(int, input().split())
for i in range(1, 11):
    if (k * i) % 10 == 0 or (k * i) % 10 == r:
        print(i)
        break
