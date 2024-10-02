###### ODEV 2 #########
from astropy.io.fits import update

##### Python_Alistirmalar  #########

### Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.
### Type() metodunu kullanınız.

x = 8
type(x)
# int

y = 3.2
type(y)
# float

z = 8j + 18
type(z)
# complex

a = "Hello World"
type(a)
# str

b = True
type(b)
# bool

c = 23 < 22
type(c)
# bool

l = [1, 2, 3, 4]
type(l)
# list

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)
# dict

t = ("Machine Learning", "Data Science")
type(t)
# tuple

s = {"Python", "Machine Learning", "Data Science"}
type(s)
# set

##### Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
## kelime kelime ayırınız.

## text = "The goal is to turn data into information, and information into insight."

text = "The goal is to turn data into information, and information into insight."
new_text = text.upper().replace(",", " ").replace(".", " ").split()
print(new_text)


##### Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E","N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)


# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

print(lst[0])
print(lst[10])


print(f"Sifirinci indeks: {lst[0]}, Onuncu indeks: {lst[10]}")


# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

new_list = lst[:4]
print(f"olusturulan liste: {new_list}")


# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
print(lst)


del lst[8]
print(f"new_list: {lst}")


# Adım 5: Yeni bir eleman ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E","N", "C", "E"]
lst.append("F")


# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")
print(lst)


##### Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.


dict = {'Christian': ["America",18],
        'Daisy': ["England",12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()
# dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])

# Adım 2: Value'lara erişiniz.

dict.values()
# dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'][1] = 13


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict['Ahmet'] = ['Turkey', 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict['Antonio']


## Görev 5: Argüman olarak bir liste alan, listenin içerisindeki
# tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def sayilar(l):
    cift_sayilar = []
    tek_sayilar = []

    for sayi in l:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
        else:
            tek_sayilar.append(sayi)
    return cift_sayilar, tek_sayilar

print("Cift sayilar:", ciftler)
print("Tek sayilar:", tekler)


##### Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


for index, ogrenci in enumerate(ogrenciler[:3], 1):
    print(f"Muhendislik Fakultesi {index}. ogrenci: {ogrenci}")
for index, ogrenci in enumerate(ogrenciler[3:], 1):
    print(f"Tip Fakultesi {index}. ogrenci: {ogrenci}")


##### Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu,
# kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjani {kontenjan} kisidir.")


##### Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise
# ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


kume1.issuperset(kume2)
# kapsamiyor




kume1.intersection(kume2)
kume2.difference(kume1)