hap = 0
cnt = 0
while True:
    age = int(input())
   
    if age >= 30:
        break
    hap += age
    cnt += 1
avg = hap / cnt
print(f"{avg:.2f}")