n = int(input())
lass = 0
line = 0
toilet = 0
for i in range(1, n+1):
    if i % 12 == 0:
        toilet += 1
    elif i % 3 == 0:
        line += 1
    elif i % 2 == 0:
        lass += 1
print(lass, line,toilet)