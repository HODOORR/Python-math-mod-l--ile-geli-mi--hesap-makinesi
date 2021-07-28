print("""*************************************

Hesap Makinesi

1.Toplama İşlemi
2.Çıkarma  İşlemi
3.Çarpma  İşlemi
4.Bölme  İşlemi
5.Üs almak için  
6.Sayının karekökünü almak için  
7.Sayının logaritması için 
8.dereceyi radyana çevirmek için 
9.radyanı dereceye çevirmek için 
10.sinüs ü bulmak için 
11.cos u bulmak için 
12.tanjantı bulmak için 
13.cotanjantı bulmak için 
 Çıkmak için q ya basın...
#sin cos tan cot bunlarda radyan cisnsinden buluyor.

*************************************
""")
import math
import time

while True:

   işlem = int(input("İşlem giriniz:"))

    if (işlem == "q"):
        print("Program sonlandırılıyor")
        time.sleep(1)
        print("Tekrar bekleriz...")
        break
    elif (işlem =="1"):
        sayı1 = int(input("Bir sayın girin:"))
        sayı2 = int(input("Bir sayı daha giriniz:"))
        print("İşleminiz yapılıyor")
        time.sleep(1)
        print("{} + {} = {} dir".format(sayı1,sayı2,sayı1+sayı2))
    elif (işlem == "2"):
        sayı1 = int(input("Bir sayın girin:"))
        sayı2 = int(input("Bir sayı daha giriniz:"))
        print("İşleminiz yapılıyor")
        time.sleep(1)
        print("{} - {} = {} dir".format(sayı1, sayı2, sayı1 - sayı2))
    elif (işlem == "3"):
        sayı1 = int(input("Bir sayın girin:"))
        sayı2 = int(input("Bir sayı daha giriniz:"))
        print("İşleminiz yapılıyor")
        time.sleep(1)
        print("{} * {} = {} dir".format(sayı1, sayı2, sayı1 * sayı2))
    elif (işlem == "4"):
        sayı1 = int(input("Bir sayın girin:"))
        sayı2 = int(input("Bir sayı daha giriniz:"))
        print("İşleminiz yapılıyor")
        time.sleep(1)
        print("{} / {} = {} dir".format(sayı1, sayı2, sayı1 / sayı2))
    elif (işlem == "5"):
        sayı1 = int(input("sayının tabanını giriniz:"))
        sayı2 = int(input("üs girin:"))
        print("İşleminiz yapılıyor")
        time.sleep(1)
        x = math.pow(sayı1,sayı2)
        print("{} üssü {} = {} ".format(sayı1, sayı2,math.pow(sayı1,sayı2)))
    elif (işlem == "6"):
        sayı1 = int(input("Bir sayın girin:"))

        print("İşleminiz yapılıyor....")
        time.sleep(1)
        x = math.sqrt(sayı1)
        print("{} sayısının karekökü = {} ".format(sayı1, math.sqrt(sayı1)))
    elif (işlem =="7"):
        sayı1 = int(input("Sayıyı girin:"))
        sayı2 = int(input("Logaritma tabanını girin:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının {} tabanında logaritması ={} ".format(sayı1,sayı2,math.log(sayı1,sayı2)))
    elif (işlem == "8"):
        sayı1 = int(input("Dereceyi giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} derece = {} radyandır".format(sayı1,sayı2,math.degrees(sayı1,sayı2)))
    elif (işlem =="9"):
        sayı1 = int(input("sayıyı girin:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} radyan = {} derecedir".format(sayı1,sayı2,math.radians(sayı1,sayı2)))
    elif (işlem == "10"):
        a = input("radyan için = R ,derece için = D basın")

        if(a == "r" or a =="R"):
            sayı1 = int(input("Sayıyı giriniz:"))
            x = math.sin(sayı1)
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            print("sin {} = {} ".format(sayı1, x))

        elif(a == "d" or a =="D"):
            sayı1 = int(input("Dereceyi giriniz:"))
            x = math.sin(sayı1)
            y = math.radians(x)
            print("İşleminiz yapılıyor")
            time.sleep(1)
            print("sin {} = {} ".format(sayı1,y))
        else:
            print("Hatalı İşlem...")
    elif (işlem =="11"):
        sayı1 = int(input("Dereceyi giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("cos {} = {}".format(sayı1,math.cos(sayı1)))
    elif (işlem =="12"):
        sayı1 =int(input("Dereceyi giriniz:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("tanjant {} = {}".format(sayı1,math.tan(sayı1)))
    elif (işlem =="13"):
        sayı1 =int(input("Dereceyi giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        x = math.cos(sayı1/math.sin(sayı1))
        print("cotanjant {} = {} ".format(sayı1,x))


