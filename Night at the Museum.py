"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

clock = "abcdefghijklmnopqrstuvwxyz"
given = input()
check = 0
time = 0
for i in range(len(given)):
    if abs(clock.index(given[i]) - check ) < 13:
        time += abs(clock.index(given[i]) - check)
        check = clock.index(given[i])
    else:
        time += 26 - abs(clock.index(given[i]) - check)
        check = clock.index(given[i])
print(time)
