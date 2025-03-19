"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    x = list(input())
    y = list(input())
    x.sort()
    y.sort()
    ans = []
    count = 0
    check = 0 
    i = 0
    j = 0

    while i < len(x) and j < len(y):
        if check == 0:  
            if count < k and (j >= len(y) or x[i] <= y[j]):
                ans.append(x[i])
                i += 1
                count += 1
            else:
                ans.append(y[j])
                j += 1
                count = 1
                check = 1
        else:  
            if count < k and (i >= len(x) or y[j] <= x[i]):
                ans.append(y[j])
                j += 1
                count += 1
            else:
                ans.append(x[i])
                i += 1
                count = 1
                check = 0

    print("".join(ans))
