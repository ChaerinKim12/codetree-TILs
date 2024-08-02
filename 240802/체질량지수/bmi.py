len, weight = map(int, input().split())
bmi = (10000*weight)/(len*len)
print(int(bmi))
if bmi > 25:
    print("Obesity")