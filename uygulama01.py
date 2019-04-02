print("*Futbol Testine Hoşgeldiniz*")
print("Aşağıdaki sorulara 'E' ya da 'H' ile cevap veriniz")
print("------------------------------------------------------------------------")
sorular = [ 'Galatasaray Süper Ligde en fazla şampiyon olan takımdır[E/H]',\
            'Süper Ligde namağlup şampiyon olan takım Fenerbahçedir[E/H]',\
            'Süper Ligde 20. şampiyonluğa ilk ulaşan takım Galatasaraydır[E/H]',\
            'İlk kurulan Türk futbol takımı Beşiktaştır[E/H]',\
            'Trabzonsporun takım renkleri siyah beyazdır[E/H],']
cevaplar = ['E', 'H', 'E', 'E', 'H']
puan = 0
#soru 1
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 2
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 3
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
print("sonucunuz:{}".format(puan*20))
#sınav sonu