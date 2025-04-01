"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy (Tricky)
        Platform: Codeforces    """

for i in range(int(input())):
    ans = 0
    a, b = map(int, input().split())
    ans += a * b
    ans += a + b
    print(ans)