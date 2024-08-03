hap = 0
cnt = 0
for _ in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        hap += a
        cnt += 1
avg = hap / cnt
print(f"{hap} {avg:.1f}")