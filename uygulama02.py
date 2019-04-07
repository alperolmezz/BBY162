print("*Sınav Soruları*")
print("Aşağıdaki soruları cevaplayınız!")
print("------------------------------------------------------------------------")
sorular = [ ' Aşağıdaki cümlelerin hangisinde '' yaşlı '' sözcüğü diğerlerinden farklı bir anlamda kullanılmıştır ?',\
            ' Aşağıdaki cümlelerin hangisinde '' geniş '' kelimesinin zıt anlamlısı kullanılmıştır ?',\
            ' Aşağıdaki cümlelerin hangisinde mecaz anlamlı sözcük yoktur ?',\
            ' Aşağıdaki cümlelerin hangisinde '' şık '' sözcüğü diğerlerinden farklı bir anlamda kullanılmıştır ?',\
            ' Aşağıdaki cümlelerin hangisinde '' güneş '' sözcüğü terim anlamıyla kullanılmıştır?']
cevaplar = ['A', 'B', 'D', 'C', 'D']

cevapA = [' Hıçkırarak yaşlı gözleriyle bana doğru baktı.',\
          ' Ağır sözler moralini bozdu.',\
          ' Çevresindekilere çok soğuk davranıyor.',\
          ' Üstüne şık bir elbise giymişti.',\
          ' Kendine yeni bir güneş gözlüğü aldı.']
cevapB = [' Oldukça sevecen yaşlı bir teyzeydi.',\
          ' Biz dar sokaklarında, dinmeyen yağmurunda geziyorduk.',\
          ' Tatlı sözleriyle yılanı deliğinden çıkardı.',\
          ' Her zaman şık birisiydi .',\
          ' Her tarafı eskimiş, güneş görmeyen bir konaktı']
cevapC = [' Mahallenin yaşlıları toplantı yaptılar.',\
          ' Çevresindekilere soğuk davranır.',\
          ' Yeni arkadaşlarıyla çabuk kaynaştı.',\
          ' Sorunu çözmek için iki şık vardı.',\
          ' Çiftçiler güneş batarken tahtadan dönüyordu.']
cevapD = [' Bu evin yaşlı sahibi vardı.',\
          ' Verimli toprakları satmayı düşünmüyoruz',\
          ' Yırtık ayakkabısını çöpe attı.',\
          ' Şık bir cevap verdi.',\
          ' Güneş gezegenlere ışık ve ısı verir.']
puan = 0
for i in range(len(sorular)):
    print("sorular"+str(i+1)+":"+sorular[i])
    print(("A") + cevapA[i])
    print(("B") + cevapB[i])
    print(("C") + cevapC[i])
    print(("D") + cevapD[i])
    cevap = input("cevabınızı lütfen buraya giriniz:")
    if(cevaplar[i] == cevap.upper()):
        puan +=1
print("sonucunuz:{}".format(puan*20))
#test sonu
