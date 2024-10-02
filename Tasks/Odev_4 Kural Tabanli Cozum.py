
######### Odev_4 Kural_Tabanli_Siniflandirma


######### PROJE GÖREVLERİ

###### Görev 1: Aşağıdaki Soruları Yanıtlayınız

## Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
pd.set_option("display.max_rows", None)

df = pd.read_csv("persona.csv")
df.head()
df.info()


## Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()



## Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()


## Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

#1
df["COUNTRY"].value_counts()

#2
df.groupby("COUNTRY")["PRICE"].count()

#3
df.pivot_table("PRICE","COUNTRY", aggfunc="count")


## Soru 5:Hangi ülkeden kaçar tane satış olmuş?

#1
df["COUNTRY"].value_counts()

#2
df.groupby("COUNTRY")["PRICE"].count()

#3
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")


## Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

#1
df.groupby("COUNTRY")["PRICE"].sum()

#2
df.groupby("COUNTRY").agg({"PRICE": "sum"})

#3
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="sum")


## Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()


## Soru 8: Ülkelere göre PRICE ortalamaları nedir?

#1
df.groupby("COUNTRY")["PRICE"].mean()

#2
df.groupby(by=['COUNTRY']).agg({"PRICE": "mean"})


# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

#1
df.groupby("SOURCE")["PRICE"].mean()

#2
df.groupby(by=['SOURCE']).agg({"PRICE": "mean"})



# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

#1
df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()

#2
df.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})


###### Görev 2:  COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

#1
df.groupby(["COUNTRY", "SOURCE","SEX", "AGE"])["PRICE"].mean().head()

#2
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()


###### Görev 3:  Çıktıyı PRICE’a göre sıralayınız.
###### Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
###### Çıktıyı agg_df olarak kaydediniz.

#1
agg_df = df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

#2
agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()



###### Görev 4:  Indekste yer alan isimleri değişken ismine çeviriniz.
###### Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
###### Bu isimleri değişken isimlerine çeviriniz.

agg_df = agg_df.reset_index()
agg_df.head()

###### Görev 5:  Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
###### Age sayısal değişkenini kategorik değişkene çeviriniz.
###### Aralıkları ikna edici şekilde oluşturunuz.
###### Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

# AGE değişkeninin nerelerden bölüneceğini belirtelim:
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim:
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

# age'i bölelim:
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()



###### Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
###### Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
###### Yeni eklenecek değişkenin adı: customers_level_based
###### Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek
###### customers_level_based değişkenini oluşturmanız gerekmektedir.


agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df = agg_df[["customers_level_based", "PRICE"]]

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df = agg_df.reset_index()

agg_df.head()


###### Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
###### Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
###### Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
###### Segmentleri betimleyiniz (Segmentlere göre groupby yapıp price"in mean, max, sum’larını alınız.)

agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=['D', 'C', 'B', 'A'])
agg_df.groupby('SEGMENT').agg({'PRICE': ['mean', 'max', 'sum']})



###### Görev 8:  Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
###### 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
###### 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
