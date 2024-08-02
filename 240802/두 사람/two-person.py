Aage, Agen = input().split()
Aage = int(Aage)
Bage, Bgen = input().split()
Bage = int(Bage)
if (Aage >= 19 and Agen == "M") or (Bage >= 19 and Bgen == "M"):
    print("1")
else:
    print("0")