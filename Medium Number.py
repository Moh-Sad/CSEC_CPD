"""
    Author: Mohammed Sadik
    Language: Python 3
    Difficulty: Easy
    Platform: Codeforces
"""

for _ in range(int(input())):
    items = list(map(int, input().split()))
    items.sort()
    print(items[1])
