from random import choice

while True:
    print('***ADAM ASMACA***')

    kelime = choice(["eskişehir", "ankara", "çanakkale", "denizli"])

    kelime = kelime.upper()
    harfsayısı = len(kelime)

    print("\nKelime {} harflidir.\n\n".format(harfsayısı))

    tahminler = []
    yanlış = []

    can = 5

    while can > 0 :

        liste=""

        for harf in kelime:
            if harf in tahminler:
                liste = liste + harf

            else:
                liste = liste +" _ "
        if liste ==kelime:
            print("Tebrikler.Doğru Bildiniz")
            break

        print("Kelimeyi tahmin edin",liste)

        print(can,"Canın Kaldı")

        tahmin = input("Bir harf giriniz\n>>>>>>>")
        tahmin = tahmin.upper()

        if tahmin == kelime:
            print("Tebrikler Doğru Bildiniz")
            break

        if tahmin in tahminler or liste in yanlış:
            print("{Daha önce yazıldı.Başka bir harf yazınız".format(tahmin))

        elif tahmin in kelime:
            rpt = kelime.count(tahmin)
            print("Doğru.{0} harfi kelimenin içinde {1} tane var".format(tahmin,rpt))
            tahminler.append(tahmin)

        else:
            print("Yanlış,Bu harf kelimenin içinde yok")
            can = can -1
    if can ==0:
        print("Tahmin hakkınız kalmadı.Kelimeyi bilemediniz")
        print("kelimemiz {}".format(kelime))

    print("Oyundan çıkmak isterseniz\n 'E' tuşuna basınız\n\nDevam etmek için başka bir tuşa basınız")
    devam = input("****")
    devam = devam.upper()

    if devam =="H":
        break

    else:
        continue






