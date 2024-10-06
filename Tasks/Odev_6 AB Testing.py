###### ODEV_6 AB Testi ile Bidding Yontemlerinin Donusumunun Karsilastirilmasi

###### Görev 1: Veriyi Hazırlama ve Analiz Etme

# Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı
# değişkenlere atayınız.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu
from streamlit import dataframe

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


df_control = pd.read_excel("ab_testing.xlsx" , sheet_name="Control Group")
df_test = pd.read_excel("ab_testing.xlsx" , sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

df_control.describe().T
df_control.head()
df_control.shape
df_test.describe().T
df_test.head()
df_test.shape


# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df_control["group"] = "control"
df_control["group"] = "test"

df_control.head()
df_control.shape
df_test.head()
df_test.shape

df = pd.concat([df_control, df_test], axis=0, ignore_index=True)
df.head()
df.tail()
df.describe()

###### Görev 2: A/B Testinin Hipotezinin Tanımlanması

# Adım 1: Hipotezi tanımlayınız.
# Bu adımda iki grup arasındaki farkı test etmek için hipotezi oluşturuyoruz:

# H0 : M1 = M2 İki grup kazanc ortalamaları arasında fark yoktur.(Null Hipotezi)
# H1 : M1!= M2 İki grup kazanc ortalamaları arasında fark vardır.(Alternatif Hipotez)


Adım 2: Kontrol ve test grubu için purchase (kazanç) ortalamalarını analiz ediniz.

df_control['Purchase'].mean()
df_test['Purchase'].mean()

# Bu noktada, ortalama değerler arasında bir fark oldugunu görebiliriz.
# Ancak, bu farkın istatistiksel olarak anlamlı olup olmadığını anlamak için hipotez testine (Görev 3) geçmemiz gerekecek.

###### Görev 3: Hipotez Testinin Gerçekleştirilmesi

# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.
# Bunlar Normallik Varsayımı ve Varyans Homojenliğidir. Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni
# üzerinden ayrı ayrı test ediniz.

# Normallik Varsayımı :

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
# p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ
# Test sonucuna göre normallik varsayımı kontrol ve test grupları için sağlanıyor mu? Elde edilen p-value değerlerini yorumlayınız.


# Kontrol grubu için normallik testi

stat_control, p_control = shapiro(df_control['Purchase'])
print(f"Kontrol Grubu - pvalue: {p_control}")

# p-value = 0.5891071186294093
# H0 REDDEDİLEMEZ. Kontrol grubunun degerleri normal dagilim varsayimini saglamaktadir.

# Test grubu için normallik testi

stat_test, p_test = shapiro(df_test['Purchase'])
print(f"Test Grubu - pvalue: {p_test}")

# p-value: 0.15413405050730578
# H0 REDDEDİLEMEZ. Kontrol grubunun degerleri normal dagilim varsayimini saglamaktadir.

# Varyans Homojenliği :

# H0: Varyanslar homojendir.
# H1: Varyanslar homojen Değildir.
# p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ
# Kontrol ve test grubu için varyans homojenliğinin sağlanıp sağlanmadığını Purchase değişkeni üzerinden test ediniz.
# Test sonucuna göre normallik varsayımı sağlanıyor mu? Elde edilen p-value değerlerini yorumlayınız.


# Varyans homojenliği testi

test_stat, p_value = levene(df_control['Purchase'], df_test['Purchase'])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, p_value))

# p-value: 0.1083 : Bu sonuç, p > 0.05 olduğu için H0 hipotezini reddedemeyeceğimizi gösteriyor.
# Sonuç: Kontrol ve test gruplarının varyansları homojendir, yani her iki grubun varyanslarının birbirine benzer olduğu sonucuna ulaşılır.



# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz.

# Normallik varsayımı sağlanırsa, Bağımsız İki Örneklem T-Testi (parametrik) kullanılır.
# Normallik varsayımı sağlanmazsa, Mann-Whitney U Testi (non-parametrik) kullanılır.

# Bağımsız iki örneklem t-testi

# Eğer normallik varsayımı sağlanırsa:


test_stat, p_value = ttest_ind(df_control['Purchase'], df_test['Purchase'], equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, p_value))


# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma ortalamaları arasında istatistiki
# olarak anlamlı bir fark olup olmadığını yorumlayınız.

# Yorum:
# p-değeri: 1.0: Bu sonuç, p > 0.05 olduğu için H0 hipotezini reddedemeyeceğimizi gösteriyor.
# Sonuç: Kontrol grubu (maximum bidding) ve test grubu (average bidding) arasında satın alma ortalamaları açısından istatistiksel olarak anlamlı bir fark yoktur.
# Bu durumda, average bidding ve maximum bidding yöntemleri arasında anlamlı bir fark bulunmamaktadır.
# Bu sonuca göre, müşteriye mevcut teklif verme yöntemi olan maximum bidding yöntemini kullanmaya devam etmeleri tavsiye edilebilir,
# çünkü yeni yöntem (average bidding) ile satın alma açısından istatistiksel olarak üstün bir sonuç elde edilmemiştir.


###### Görev 4: Sonuçların Analizi

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz

# Normallik sağlandığı ve varyanslar homojen olduğu için, Bağımsız İki Örneklem T-Testi bu tür durumlar için en uygun testtir.
# Test sonucunda elde edilen p-değeri, iki grup arasında anlamlı bir fark olup olmadığını gösterir.
# Bu testin uygulanması, iki grup arasında istatistiksel olarak anlamlı bir fark olup olmadığını anlamak için en doğru yöntemdir.


# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

# Müşteriye, average bidding yöntemi ile maximum bidding yöntemi arasında satın alma performansı açısından anlamlı bir fark bulunmadığını, dolayısıyla mevcut yöntem olan maximum bidding'e devam etmelerinin mantıklı bir seçim olduğunu önerebiliriz.
# Ancak maliyet açısından bir avantaj varsa, average bidding ile testlere devam edilebilir.