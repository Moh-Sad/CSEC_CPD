"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

shoes = list(map(int, input().split()))
shoes = set(shoes)
print(4 - len(shoes))
