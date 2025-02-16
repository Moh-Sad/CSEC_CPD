"""
    Author: Mohammed Sadik
    Language: Python 3
    Difficulty: Easy
    Platform: Codeforces
"""

for _ in range(int(input())):
    items = list(map(int, input().split()))
    count = 0
    for i in range(len(items)):
        if items[0] < items[i]:
            count += 1
    print(count)
