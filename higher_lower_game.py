import random
def newnumber():
    global thenumber
    thenumber = random.randint(1,501)
print("  ---*** Sayı Tahmin Oyunu ***---  \n\n 1 ve 500 arasında rastgele bir sayı \n\n")
newnumber()
def guesstime():
    guess = int(input("Bir Sayı Giriniz: "))
    if guess < thenumber:
        print("Yükselt")
        guesstime()
    elif guess > thenumber:
        print("Düşür")
        guesstime()
    elif guess == thenumber:
        res = int(input("Tebrikler! Tekrar oynamak için 1 çıkış için 0: "))
        if res == 1:
            newnumber()
            guesstime()
        else:
            None
    else:
        print("Lütfen geçerli bir sayı girin")
        guesstime()

guesstime()