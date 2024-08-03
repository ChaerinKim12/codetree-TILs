hap = 0
cnt = 0

while True :
    n = int(input())

    if n // 10 % 10 != 2 : 
        break
    hap += n
    cnt += 1

print(f"{hap/cnt:.2f}")