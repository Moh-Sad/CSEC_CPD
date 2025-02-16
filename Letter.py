"""
    Author: Mohammed Sadik
    Language: Python 3
    Difficulty: Medium
    Platform: Codeforces
"""

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
t,b = n,0
l,r= m,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":
            t = min(t, i)
            b = max(b, i)
            l = min(l, j)
            r = max(r, j)
for k in range(t, b + 1):
        print("".join(arr[k][l:r + 1]))
