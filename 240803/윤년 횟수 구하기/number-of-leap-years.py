a = int(input())
dbssus = 0
vudsus = 0
for i in range(1, a+1):
    if i % 4 == 0:
        if (i % 100 == 0) and (i % 400 != 0):
            vudsus += 1
        else:
            dbssus += 1
print(dbssus)