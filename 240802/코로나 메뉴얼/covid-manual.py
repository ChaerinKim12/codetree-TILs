Acold, An = input().split()
An = int(An)
Bcold, Bn = input().split()
Bn = int(Bn)
Ccold, Cn = input().split()
Cn = int(Cn)
cnt = 0
if Acold == "Y" and An >= 37:
    cnt += 1
if Bcold == "Y" and Bn >= 37:
    cnt += 1
if Ccold == "Y" and Cn >= 37:
    cnt += 1
if cnt >= 2:
    print("E")
else:
    print("N")