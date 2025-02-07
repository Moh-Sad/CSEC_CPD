"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Medium
Platform: Codeforces    
"""
home = []
guest = []
count = 0

for i in range(int(input())):
    h, g = map(int, input().split())
    home.append(h)
    guest.append(g)
for j in range(len(home)):
    count += guest.count(home[j])

print(count)
