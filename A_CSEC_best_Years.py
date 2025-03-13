"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

num = input()
items = list(map(int, num.split()))
while True:
    num = int(num) + 1
    num = str(num)
    items = list(num)
    check = len(set(items))
    if check == 4:
        print(num)
        break