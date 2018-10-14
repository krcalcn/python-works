num = int(input("Bir Sayı Giriniz: "))
if  num%2 == 0:
    num = num + 1
for a in range(1,num,2):

    for b in range(num-1,a,-2):
        print(" ", end='')

    for x in range(a):
        print("*", end='')
    print("")
for y in range(num-4,-1,-2):
    for z in range(y,num,2):
        print(" ", end='')
    for c in range(y):
        print("*", end='')
    print("")