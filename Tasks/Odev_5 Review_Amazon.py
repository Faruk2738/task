###################################################
# Odev 5: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# Veri Seti Hikayesi
###################################################

# Amazon ürün verilerini içeren bu veri seti ürün kategorileri ile çeşitli metadataları içermektedir.
# Elektronik kategorisindeki en fazla yorum alan ürünün kullanıcı puanları ve yorumları vardır.

# Değişkenler:

# reviewerID        : Kullanıcı ID’si
# asin              : Ürün ID’si
# reviewerName      : Kullanıcı Adı
# helpful           : Faydalı değerlendirme derecesi
# reviewText        : Değerlendirme
# overall           : Ürün rating’i
# summary           : Değerlendirme özeti
# unixReviewTime    : Değerlendirme zamanı
# reviewTime        : Değerlendirme zamanı Raw
# day_diff          : Değerlendirmeden itibaren geçen gün sayısı
# helpful_yes       : Değerlendirmenin faydalı bulunma sayısı
# total_vote        : Değerlendirmeye verilen oy sayısı

import matplotlib.pyplot as plt
import pandas as pd
import math
import scipy.stats as st
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 10)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)



###### GÖREV 1: Average Rating'i güncel yorumlara göre hesaplayınız ve var olan average rating ile kıyaslayınız.

# Paylaşılan veri setinde kullanıcılar bir ürüne puanlar vermiş ve yorumlar yapmıştır. Bu görevde amacımız verilen puanları tarihe göre ağırlıklandırarak değerlendirmek.
# İlk ortalama puan ile elde edilecek tarihe göre ağırlıklı puanın karşılaştırılması gerekmektedir.


###### Adım 1: Ürünün ortalama puanını hesaplayınız.

df = pd.read_csv("amazon_review.csv")
df.head()
df["overall"].mean()



###### Adım 2: Tarihe Göre ağırlıklı puan ortalamasını hesaplayınız.


# day_diff: yorum sonrası ne kadar gün geçmiş

df['reviewTime'] = pd.to_datetime(df['reviewTime'], dayfirst=True)
current_date = pd.to_datetime(str(df['reviewTime'].max()))

# df["day_diff"] = (current_date - df['reviewTime']).dt.days

df.loc[df["day_diff"] <= df["day_diff"].quantile(0.25), "overall"].mean() # 4.696
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.25)) & (df["day_diff"] <=
df["day_diff"].quantile(0.50)), "overall"].mean() # 4.64
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.50)) & (df["day_diff"] <=
df["day_diff"].quantile(0.75)), "overall"].mean() # 4.57
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.75)), "overall"].mean() # 4.45

# zaman bazlı ortalama ağırlıkların belirlenmesi

def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
return dataframe.loc[dataframe["day_diff"] <=
dataframe["day_diff"].quantile(0.25), "overall"].mean() * w1 / 100 + \
dataframe.loc[(dataframe["day_diff"] >
dataframe["day_diff"].quantile(0.25)) & (dataframe["day_diff"] <=
dataframe["day_diff"].quantile(0.50)), "overall"].mean() * w2 / 100 + \
dataframe.loc[(dataframe["day_diff"] >
dataframe["day_diff"].quantile(0.50)) & (dataframe["day_diff"] <=
dataframe["day_diff"].quantile(0.75)), "overall"].mean() * w3 / 100 + \
dataframe.loc[(dataframe["day_diff"] >
dataframe["day_diff"].quantile(0.75)), "overall"].mean() * w4 / 100
df.loc[df["day_diff"] <= df["day_diff"].quantile(0.25), "overall"].mean() * 28 /
100 + \
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.25)) & (df["day_diff"] <=
df["day_diff"].quantile(0.50)), "overall"].mean() * 26 / 100 + \
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.50)) & (df["day_diff"] <=
df["day_diff"].quantile(0.75)), "overall"].mean() * 24 / 100 + \
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.75)), "overall"].mean() * 22 /
100
time_based_weighted_average(df, w1=28, w2=26, w3=24, w4=22) # 4.59559316512811
df["overall"].mean() # 4.58



###### Görev 2: Ürün için ürün detay sayfasında görüntülenecek 20 review'i belirleyiniz.

###### Adım 1. helpful_no değişkenini üretiniz.

# total_vote bir yoruma verilen toplam up-down sayısıdır.
# up, helpful demektir.
# veri setinde helpful_no değişkeni yoktur, var olan değişkenler üzerinden üretilmesi gerekmektedir.
# Toplam oy sayısından (total_vote) yararlı oy sayısı (helpful_yes) çıkarılarak yararlı bulunmayan oy sayılarını (helpful_no) bulunuz.

df.head()
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]


###### Adım 2. score_pos_neg_diff, score_average_rating ve wilson_lower_bound skorlarını hesaplayıp veriye ekleyiniz.

def wilson_lower_bound(up, down, confidence=0.95):

    n = up + down
    if n == 0:
    return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)
    def score_up_down_diff(up, down):
    return up - down
    def score_average_rating(up, down):
    if up + down == 0:
    return 0
    return up / (up + down)


# score_pos_neg_diff

df.head(20)
df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_pos_neg_diff", ascending=False).head(20)

# score_average_rating

df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_average_rating", ascending=False).head(20)


df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("wilson_lower_bound", ascending=False).head(20)


###### Adım 3. 20 Yorumu Belirleyiniz ve Sonuçları Yorumlayınız.

df.sort_values("wilson_lower_bound", ascending=False).head(20)