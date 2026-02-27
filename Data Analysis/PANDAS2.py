import pandas as pd
"""
#DATAFRAME GROUPBY
#VEERİLERİ GRUPLAYIP İŞLEM YAPMADIR çoğu şeyi yaparsın mesela büyük veeri var maaşlar üzerinde işlem yapcan onu seçersin gibi gibi
# Örnek veri
data = {
    "Departman": ["IT", "IT", "HR", "HR", "Finans", "Finans"],
    "Çalışan": ["Ali", "Ayşe", "Mehmet", "Elif", "Ahmet", "Zeynep"],
    "Maaş": [15000, 17000, 12000, 12500, 20000, 22000]
}
df = pd.DataFrame(data)

print("Veri:")
print(df)
print("----")

# Departmanlara göre toplam maaş
print("\nDepartmanlara göre toplam maaş:")
print(df.groupby("Departman")["Maaş"].sum())

result = df.groupby("Departman")["Maaş"].agg(["sum", "mean", "median"])
print(result)
#--------------------------------------------------
"""
"""
#PANDAS İLE KAYIP VE BOZUK VERİ ANALİZİ

df.drop("column1", axis = 1) #silme işlemi ama axis belirtmen lazım  sutün
df.isnull() # bu parametre Nan olan değerleri true yapar
df.notnull() #bu ise dolu ları true yapar 
df.isnull().sum() #kaç boş değer var 
df["column1"].isnull() # 1 deki değerler
df.dropna("column1", axis=0) #nan içerren satırı yazma bide axis 0 yazmana gerek yok zaten normalde 0 ı gösterir
# dropna kımına (subset = diyerek hangi sutunlarda sadece işlem yapmak istediğini belirtebilirsin)
# dropna kısmında dropna(how = all) felan diyerek satırın veya sutunun tamamı null ise onu sil diyebilirsin how işlemi nasıl ilem almak istedğini gösteri
# dropna (thresh =4) demek osatırda 4 tane veri var ise yazdır
#df.fillna() Pandas DataFrame’deki eksik değerleri (NaN) doldurmak için kullanılır.
"""
#----------------------------------------------------------

#PANDAS İL STRİNG FONKSİYONLARI 
"""
import pandas as pd 
import pandas as np 

data = pd.read_csv("sarj_verisi.csv")
data = data.dropna() #eksik bir nan var ise o satırı siler axis = 1 de ise sutünü siler 
print(data.columns) #hangi kolonlar var
#data["AracID"] = data["AracID"].str.upper() # arac ID hepsini büyük harf yapar böyle yaparak o kolon üzerinden string işlemler yapabilirsin.
#data["AracID"] = data["AracID"].str.lower() #kücük harf 
#data = data[data.AracID.str.contains("EV1000")] #ev1000 olan satırları ver 
data = data.AracID.str.replace("E","M") # e leri m ile değiş 
#üsteki 2 örnekte görüldüğü üzere birinde 3 data dierined 2 data sebebi 1.de ilk önce data.aracıd bu tüm sutunları true false yapar .2 data true falseli datayı yeni veri diye alır kendine 3. data ise printlemek için
#2. örnek ise data arac.ıd kolonunun seçer ve e ile m yi değişip dataya atar 
print(data)

"""
#---------------------------------------------

#PANDAS İLE JOİN VE MERGE

#merge → Pandas’ta iki tabloyu (DataFrame) birleştirmek için kullanılır. Kolon isimlerine göre eşleştirir.
#join → Bir DataFrame’i diğerine indeks veya kolon üzerinden ekleme yapmak için kullanılır. Genelde df1.join(df2) şeklinde kullanılır.

import pandas as py
import numpy as np
"""
Musteri = {
    "MusteriID" : [1,3,7,8],
    "İsim" : ["Melih","Selim","Tarık","Ece"],
    "Soyisim" : ["Doğan","Aydın","Celik","Turan"]
}

Siparis = {
    "MusteriID" :[1,4,6,8],
    "SiparidID" : [2,3,4,5],
    "Siparis_Tarih" : ["10.01.2005","10.11.2008","04.01.2003","28.06.2015"]
  

}

data = pd.DataFrame(Musteri)
data1 = pd.DataFrame(Siparis)
print(data)
print(data1)

result  = pd.merge(data,data1,how="inner") #Sadece her iki tabloda da ortak olanları alır.
print(result)
result  = pd.merge(data,data1,how="left"),#Sol tablodaki tüm satırları alır, sağ tabloda eşleşmeyen varsa NaN olur.
print(result)
result  = pd.merge(data,data1,how="right")#Sağ tablodaki tüm satırları alır, sol tabloda eşleşmeyen varsa NaN olur.
print(result)
#result  = pd.merge(data,data1,how="outer")# sağ ve soldaki buyun kayıtları getirir
# pd.concat() iki tane tabloyu birleştirir. **
"""

#---------------------------------------------------------------------------

#PANDAS İLE DATAFRAME METODLARI:
"""
df.unique() #sutündaki eelemanları verir ama tekrarlayanları vermez 3 tane 20 var 1 tane vereir 20
df.nunique() #sayısıını verir
df.value_counts() # ne kaç kez tekrarlamış verir
df.apply(kareal) #bu diyelim kareal fonk var butun hücreleri tek tek o fonka gönderir 
df.pivot_table() # bunla elinde bir tablo varsa onu değiştirebilirsin mesela indexi ay kolonları satır gibi değişiklikler 
"""