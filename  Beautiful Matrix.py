"""     
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
Platform: Codeforces    
"""

round = 0
answer = 0
check = False
while True:
    items = list(map(int, input().split()))
    if 1 in items:
        place = items.index(1)
        if place == 0 or place == 4:
            answer = 4 - round
            break
        elif place == 1 or place == 3:
            answer = 3 - round
            break
        else:
            answer = 2 - round
            break
    else:  
        if round == 2 and check == False:
            round = 1
            check = True
        elif check == True:
            round = 0
        else:  
            round += 1      
print(answer)