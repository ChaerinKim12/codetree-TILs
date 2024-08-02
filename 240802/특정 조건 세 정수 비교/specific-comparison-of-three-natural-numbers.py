# 세 개의 정수를 입력받습니다.
a, b, c = map(int, input().split())

# 가장 작은 수를 찾고, 그 수가 a와 같은지 비교합니다.
if a < b and a < c:
    print("1", end=" ")
elif b < a and b < c:
    print("0", end=" ")
elif c < a and c < b:
    print("0", end=" ")

# 세 수가 모두 같은지 확인합니다.
if a == b and a == c:
    print("1")
else:
    print("0")