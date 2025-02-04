"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy
        Platform: Codeforces     """

number_of_problems = int(input())
solved_problems = 0
for i in range(number_of_problems):
    problems = list(map(int, input().split()))
    if problems[0] == 1 and problems[1] == 1:
        solved_problems += 1
    elif problems[1] == 1 and problems[2] == 1:
        solved_problems += 1
    elif problems[0] == 1 and problems[2] == 1:
        solved_problems += 1
print(solved_problems)