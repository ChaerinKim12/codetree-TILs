n = int(input())
hap = 0
for _ in range(n):
    a = int(input())
    if a % 3 == 0 and a % 2 == 1:
        hap += a
print(hap)