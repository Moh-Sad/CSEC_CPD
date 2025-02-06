"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

n = int(input())
count = 1
check = 'empty'

for i in range(n):
    magnet = input()

    if check == 'empty':
        check = magnet[0]
    elif int(check) != int(magnet[0]):
        count += 1
    
    check = magnet[0]

print(count)
