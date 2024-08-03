a,b = map(int, input().split())
hap = 0
cnt = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        hap += i
        cnt += 1
avg = hap / cnt
print(hap, end=" ")
print(f"{avg:.1f}")