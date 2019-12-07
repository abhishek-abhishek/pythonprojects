print("\t Shapes")

for i in range(1,11):
    for j in range(11-i):
        print(" ",end = " ")
    for j in range(1,i):
        print("W00",end = " ")
    for i in range(i,0,-1):
        print("S00",end = " ")
    print()
for i in range(11):
    for j in range(i+2):
        print(" ",end = " ")
    for j in range(1,10-i):
        print("T00",end = " ")
    for j in range(8-i,0,-1):
        print("Z00",end = " ")
    print()
