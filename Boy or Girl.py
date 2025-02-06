"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""

username = input()
username = set(username)

if len(username) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
