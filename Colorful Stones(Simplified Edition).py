"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

step = input()
instruction = input()
place = step[0]
count = 1
j = 1
for i in range(len(instruction)):
    if instruction[i] == place:
        place = step[j]
        count += 1
        j += 1
print(count)
