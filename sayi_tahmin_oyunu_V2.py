import random
import sys
###fonksiyon tanımları###
def yeni_oyun():
    print('Yeni Oyun!!!')
    sayi = random.randint(1, 20)
    tahmin = input("Tahmininizi yaziniz\n"
                   "Hile modeu için 'S-s'e\n"
                   "Debug mode için 'D-d'e\n"
                   "Hareket mode icin 'M-m'e\n"
                   "Yeni oyun için 'N-n'e \n"
                   "Oyundan çıkmak isterseniz 'X-x'e basınız: ")

def hile_modu():
    print('Hile modu!!!')
    print(sayi)


def debug_mod():
    print("Debug mode acildi!!!")
    print(sayi)
    global tahmin
    while True:
        tahmin = input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,"
                           "Debug mode kapamak için 'D-d' basınız!): ")
        if tahmin == 'D' or tahmin == 'd':
            print("Debug mode kapandı!!!!")
            break

def hareket_modu():
    print('Hareket modu acildi!!!')
    print(sayi)
    global tahmin
    randomx = random.randint(0, 1)
    if randomx == 1:
        print(sayi + 2)
    if randomx == 0:
        print(sayi - 2)
    while True:
        tahmin = input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,"
                       "Hareket mode kapamak için 'M-m' basınız!): ")
        if tahmin == 'M' or tahmin == 'm':
            print("Hareket mode kapandı!!!!")
            break
def cikis():
    sys.exit('program sonlandı!!')

### kullanıcıdan giriş isteme ###
print("Hile modeu için 'S-s'e\n"
       "Debug mode için 'D-d'e\n"
       "Hareket mode icin 'M-m'e\n"
       "Yeni oyun için 'N-n'e \n"
       "Oyundan çıkmak isterseniz 'X-x'e basınız ")
while True:
    sayi = random.randint(1, 20)
    tahmin = input("Tahmininizi yaziniz (Çıkmak için 'X-x' basınız):")

    if tahmin == 'N' or tahmin == 'n':
        yeni_oyun()
    if tahmin == 'S' or tahmin == 's':
        hile_modu()
    if tahmin == 'D' or tahmin == 'd':
        debug_mod()
    if tahmin == 'M' or tahmin == 'm':
        hareket_modu()
    if tahmin == 'X' or tahmin == 'x':
        cikis()
    #eğer girilen harf degil sayı ise tahmin int olarak alınacak ve karşılaştırma yapılacak

    if (tahmin != 'M' or tahmin != 'm') and (tahmin != 'X' or tahmin != 'x') and (tahmin != 'N' or tahmin != 'n') and (tahmin != 'S' or tahmin != 's') and (tahmin != 'D' or tahmin != 'd'):
        tahmin = int(tahmin)
        if tahmin > sayi:
            print('Tahmininiz sayidan daha büyük')
            tahmin = input("Tahmininizi yaziniz (Çıkmak için 'X-x' basınız):")
        elif tahmin < sayi:
            print('Tahminininz sayidan daha küçük')
            tahmin = input("Tahmininizi yaziniz (Çıkmak için 'X-x' basınız): ")
        else:
            print('Tahmininiz sayi ile eşit')
            break
