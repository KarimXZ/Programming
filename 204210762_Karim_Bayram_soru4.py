#capitalize():Birinci harfi buyukluyor.Sonuc:Karim
x="karim"
x.capitalize()
print(x)
#casefold():Her harflari kucukluyor. Sonuc:karim
x="Karim"
x.casefold()
print(x)
#center():Bosluk yadziriyor ve bosluklarin arasinda str koyuyor.iki parametre var:
#Birinci boslugun sayisi, ve ikinici boslugun tipi.
y=x.center(30,'k')
print(y)
#count():Str icindeki ozel harfi sayiyor.Sonuc:1
print(x.count("K"))
#encode():UTF-8 kullanarak str sifreliyor.
print(x.encode())
#endswith():Bool metod, str`in sonucta ozel harf varsa True donduruyor.Sonuc:True
print(x.endswith('m'))
#expandtabs():/t metod var strler icinde, tab(4bosluk) koyuyor. Bu metod boslugun 
#sayisi degistiryor.
x="K\tarim"
print(x.expandtabs(12))
#find():str icinde ozel harf buluyor, onun konusu donduruyor. ayni harf iki kez
# bulunursa sadece birinciyi tarif edilir.
print(x.find('a'))
#format():Degiskenler str icinde koymak icin.
x="dondurma simdi {fiyat} lira"
print(x.format(fiyat=5))
#format_map():Format gibi, ama dic icin.
#index():find() gibidir, ama find() calismazsa program baslamiyor. Index -1 dondurur.
x.index('K')
#Asagidaki fonksiyonlar benzerdir, hepsini bool fonksionlar str tipi duzenliyorlar
# isalnum():Alphanumeric ise True, yaane ozel karakterler yok.(#$%^ gibi)
# isalpha():Alphabetic ise True, yaane sadece harflar var
# isdecimal():Sadece onluluk sayilar var(kesirler yok)
# isdigit():sadece sayilar var
# islower():sadece kucuk harflar var
# isnumeric():sadece sayilar var veya sayi isaret eden seyler var
# isprintable():ozel metodlar (\t\n\r) yoksa True donduruyor

#join():str ve tuple, set, veya dic eklemek icin join kullanilir

#ljust():center() gibi, ama str sol tarafta koyulacak

#lower():casefold() gibi, ama sadece ASCII karakterler ile

#lstrip(): soldaki bosluklar siliyor

#replace():str icindeki hard ya da kelime degistiriyor. ucuncu parametre kac kere
#icin kullanilabilir.

#rfind(): find() gibi, ama sagdan basilyor

#rindex(): index gibi, ama sagdan basliyor

#rpartition(): partition(): ozel harf ya da kelime buluyor, ve bu ozelin gore str uc parca
#kestiryor. Yeni parcalar tuple olacak. rpartition(): partition gibi ama sagdan
#basliyor

#split(): strdeki kelimler aliyor listte koyuyor. Parametre degistirilebilir, ama
#normal olarak bosluk kullaniyor str kestirmek icin.

#startswith():endswith() gibi, ama baslangic icin.

#strip():sag ve soldaki bosluklar siliyor.

#zfill():strin baslangicta sifirlar koyuyor.