"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

a = input()
b = input()

a = a.upper()
b = b.upper()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
