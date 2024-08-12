n = int(input())
satisfied = False
for i in range(1, n+1):
    if i % 1 == 0 and i % n == 0:
        satisfied = True
if satisfied == True:
    print("P")
else:
    print("C")