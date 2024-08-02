a, b, c = map(int, input().split())
if a < b and a < c:
    if a == a:
        print("1", end=" ")
    else:
        print("0", end=" ")
elif b < a and b < c:
    if a == b:
        print("1", end=" ")
    else:
        print("0", end=" ")
elif c < a and c < b:
    if a == c:
        print("1", end=" ")
    else:
        print("0", end=" ")
if a == b and a == c and b == c:
    print("1")
else:
    print("0")