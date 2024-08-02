# 입력 받기
N = int(input())
numbers = []

for _ in range(N):
    num = int(input())
    numbers.append(num)

# 홀수이면서 3의 배수인 수들을 출력
for num in numbers:
    if num % 2 != 0 and num % 3 == 0:
        print(num)