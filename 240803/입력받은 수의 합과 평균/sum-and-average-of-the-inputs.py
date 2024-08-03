n = int(input())
hap = 0
cnt = 0
for _ in range(n):
    a = int(input())
    hap += a
    cnt += 1
avg = hap / cnt
print(f"{hap} {avg:.1f}")