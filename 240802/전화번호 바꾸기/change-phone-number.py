# 입력값을 받습니다. 예를 들어 "010-1234-5678"
input_string = input()

# '010-'을 제거하고 나머지 부분을 '-'로 분리합니다.
_, a, b = input_string.split('-')

# 새로운 형식으로 출력합니다.
print("010-{}-{}".format(b, a))