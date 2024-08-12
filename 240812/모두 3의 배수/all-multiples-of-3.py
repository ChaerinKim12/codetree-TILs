value = 0
for _ in range(5):
    n = int(input())
    if n % 3 == 0:
        value = 1
    else:
        print("0")
        value = 0
        break
if value == 1:
    print("1")