for _ in range(int(input())):
    check = True
    num = int(input())
    count = 0
    items = list(map(int, input().split()))
    for i in range(num):
        if items[i] < 0 and check == True:
            count += 1
            check = False
            items[i] = abs(items[i])
        elif items[i] > 0:
            check = True
        else:
            items[i] = abs(items[i])
    print(sum(items), count)