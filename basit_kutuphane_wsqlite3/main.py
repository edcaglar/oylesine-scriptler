from kutuphane import *

print("""*************************************

Kutuphane Programina Hosgeldiniz.

Islemler:

1. Kitaplari Goster

2. Kitap Sorgula

3. Kitap Ekle

4. Kitap Sil

5. Baski Yukselt

Cikmak icin 'q' ya basin.
*************************************""")

kutuphane = Kutuphane()

while True:

    islem = input("Yapacaginiz islem:")

    if (islem == 'q'):

        print("Program Sonlandiriliyor")
        break

    elif (islem == "1"):

        kutuphane.kitaplari_goster()

    elif (islem == "2"):

        isim = input("Hangi kitabi sorgulamak istiyorsunuz ?")
        print("Kitap Sorgulaniyor ...")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):

        isim = input("Isim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayinevi :")
        tur = input("Tur:")
        baski = int(input("Baski: "))

        kitap = Kitap(isim, yazar, yayinevi, tur, baski)
        print("Kitap ekleniyor ...")
        time.sleep(2)

        kutuphane.kitap_ekle(kitap)
        print("Kitap eklendi....")

    elif (islem == "4"):
        isim = input("Hangi kitabi silmek istiyorsunuz: ")
        cevap = input("Emin misiniz ? (E/H)")

        if(cevap == 'E'):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi")
        else:
            print("Silinmedi")

    elif (islem == "5"):
        isim = input("Hangi kitabin baskisini yukseltmek istiyorsunuz ?")
        print("Baski yukseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        

    else:
        print("Gecersiz Islem")
