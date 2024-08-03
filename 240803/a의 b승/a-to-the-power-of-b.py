a, b = map(int, input().split())
wprhq = 1
for i in range(1, b+1):
    wprhq *= a
print(wprhq)