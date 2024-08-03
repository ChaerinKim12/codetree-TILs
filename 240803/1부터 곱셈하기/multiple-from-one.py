n = int(input())
sol = 1
for i in range(1, 11):
    sol *= i
    if sol >= n:
        print(i)
        break