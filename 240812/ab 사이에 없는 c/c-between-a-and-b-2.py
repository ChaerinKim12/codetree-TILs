satisfied = True
a, b, c = map(int, input().split())
for i in range(a, b):
    if i % c != 0:
        satisfied = False
if satisfied == True:
    print("NO")
else:
    print("YES")