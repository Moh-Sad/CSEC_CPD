"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

for _ in range(int(input())):
    n = int(input())
    bag = list(map(int, input().split()))
    bag.sort()
    check = bag[0]
    ans = -1
    count = 1
    for i in range(1,n):
        if check == bag[i]:
            count += 1
        else:
            if count > 2:
                ans = check
                break
            check = bag[i]
            count = 1
        if count > 2:
                ans = check
                break
    print(ans)