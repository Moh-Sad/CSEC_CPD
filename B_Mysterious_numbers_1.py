"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy (Tricky)
        Platform: Codeforces    """

a, b = map(str, input().split())
b = list(b)
b = b[::-1]
b = ''.join(b)
print(int(a) + int(b))