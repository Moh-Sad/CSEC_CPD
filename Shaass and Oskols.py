"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Medium
        Platform: Codeforces    """

n = int(input())
wire = list(map(int, input().split()))
for j in range(int(input())):
    a, b = map(int, input().split())
    if a > 1:
        wire[a - 2] += b - 1
    if a < n:
        wire[a] += wire[a - 1] - b
    wire[a - 1] = 0
for i in range(n):
    print(wire[i])