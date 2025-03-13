"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""
ans = 0
for _ in range(int(input())):
    items = list(map(int, input().split()))
    check = items.count(1)
    if check > 1:
        ans += 1
print(ans)