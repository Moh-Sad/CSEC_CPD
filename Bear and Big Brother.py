"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy
        Platform: Codeforces    """

limak_weight, bob_weight = map(int, input().split())
year_count = 0
while True:
    if limak_weight > bob_weight:
        print(year_count)
        break
    else:
        limak_weight *= 3
        bob_weight *= 2
        year_count += 1