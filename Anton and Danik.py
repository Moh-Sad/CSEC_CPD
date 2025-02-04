"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy
        Platform: Codeforces    """

number_of_games = int(input())
items = list(input())
anton_wins = 0
danik_wins = 0
for i in range(number_of_games):
    if items[i] == "A":
        anton_wins += 1
    else:
        danik_wins += 1
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")