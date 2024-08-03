def division_steps(n):
    count = 0
    divisor = 1
    while n > 1:
        divisor += 1
        n = n // divisor
        count += 1
    return count

# 입력 받기
n = int(input().strip())
# 결과 출력
print(division_steps(n))