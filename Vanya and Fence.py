"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy        """

n, h = map(int, input().split())
items = list(map(int, input().split()))
count = 0
for i in range(n):
    if items[i] > h:
        count += 2
    else:
        count += 1
print(count)