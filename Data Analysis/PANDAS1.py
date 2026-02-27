"""
Pandas, Python programlama dili için geliştirilmiş, özellikle veri analizi ve veri manipülasyonu (işleme, düzenleme, dönüştürme) için kullanılan en popüler kütüphanelerden biridir.

Ne işe yarar?

Tablo benzeri veri yapıları sağlar → En önemlisi DataFrame (Excel tablosuna benzer). Satır-sütun şeklinde veriler üzerinde kolayca işlem yapabilirsin.

Veri temizleme → Eksik verileri doldurma, silme, dönüştürme.

Veri seçme ve filtreleme → İstediğin sütunu/koşulu seçebilirsin.

İstatistiksel işlemler → Ortalama, toplam, standart sapma gibi hızlı hesaplamalar.

Veri dönüştürme → Veriyi yeniden şekillendirme (pivot, groupby).

Dosya okuma ve yazma → CSV, Excel, SQL, JSON gibi formatlardan veri alabilir ve kaydedebilir.

"""
"""
#1.PANDAS SERİES
import pandas as pd
import numpy as np

numbers = [20,30,40,50]
dict = {'a':10,'b':20,'c':30}
pandas_series = pd.Series(numbers) # 0 a 20 1 e 30 2ye 40 gclelir
pandas_series = pd.Series(numbers, ['a','b','c','d']) # cevabı aya 20 bye 30 cye 40 gelir
pandas_series = pd.Series(dict) #zaten a karşısında 10 diye a10 b20 c 30 çıkar

opel2018 = pd.Series([20,30,40,50],['astra','polo','insignie','mokka'])
opel2025 = pd.Series([220,302,430,10],['astra','corsa','grönland','mokka'])

total = opel2018 + opel2025
print(total)
print(total['astra']) 
"""
#---------------------------------------
"""
#2.PANDAS DATAFRAMES
#İki boyutlu, satır ve sütunlardan oluşan tablo benzeri bir veri yapısıdır.
#2 veya daha çok serinin toplamıdır birçok sutün olur

import pandas as pd
import numpy as np

#bu kısım ana mantığı işin yani 2 tane seriden gelir dict olması lazım felan
s1 = [0,1,2,4,5]
s2 = [4,2,68,9,8]
data = dict(apples = s1, oranges = s2)
df = pd.DataFrame(data)
print(df)
"""
#NOT:istersek columns, index ve dype nin isimlerini kendimiz koyabiliriz.
#bir list veya dict yapısını df.DataFrame(dict) felan yazarak onu data framelerine ayırabilirsin

#----------------------------------------------------------
"""
#3Pandas ile farklı dosya tiplerinden veri okuma 

df = pd.read_csv('melih.csv') #csv dosyası okuma
df = pd.read_json('melih.json', encoding="UTF-8") #json okur ve türkçe karekterleride kapsar
df = pd.read_excel('melih.xlsx') #excel okur
#veri tabanından da veri çekebiliyoruz pd.read_sql_query gibi ama sql bağlanman lazım
#print(df) 
"""
#---------------------------------------------------
"""
#4ÇALIŞMA
# birçok kolon çıkıyor her kolonu ve satırı ayrı ayrı kodla çekebiliriz df.loc ile 
 # df.loc[ satır_seçimi , sütun_seçimi ] (:) tümünü seç anlamına gelir 
 #df.iloc ise index üzerinden çalışma demek 
result = df.loc("A","Column2") # A satır 2.colomn 2 deki değer gelir 
df["Column4"] = pd.Series(randn(3), ["A","B","C"]) #yeni bir tane colons
df['Column5'] = df['Column1'] + df['Column3'] #kolon5 1 le 3 ün toplamı olur 
df.drop("Column4", axis=1) #5. kolonu siler axis=1 sutun axis=0 satır demek belirtmen lazım
"""
#------------------------------------------------
"""
#ÖNEMLİ
#5DATAFRAME FİLTRELEME
import pandas as pd 
import numpy as np

data = np.random.randint(10,100,80).reshape(10,8)
df = pd.DataFrame(data, columns= ["A","B","C","D","E","F","G","H"])
result = df.columns #colonların isimleri liste halinde verir
result2 = df.head(5) # ilk beş satırı kayıdı verir
result3 = df.tail(5) # son 5 satır
result4 = df["A"].head(3) #A kolonu 3 kaydı önüne getirir
result5 = df[["A","B"]] # 2 TANE kolonu verir 
result6 = df[5:10][["A","B"]] #A VE B KOLONUN 5 İLE 10 ARASI SATIRINI AL
#filtreleme
result7 = df > 20 #20den büyüklere true değillere false gelir 
result8 = df[df > 20] # true false yerine değerleri verir küçüklere NAN verir
result9 = df["A"] > 20 # sadece kolon A işleme alır true false bir df daha eklersen sayı değeri verir
result10 = df.query("A > 20 & B < 50") # kosul işlem bütün kolonları verir
result11 = df.query("A > 20 & B < 50")[["A","B","G"]] #sadece a b g kolonunu verir yani her szaman ilk baştaki koşul 2. ise list olur 
print(result10)
"""

#NOT: 2 ve daha fazla kolon gönderdiğin zaman 2 tane [] kullan
#NOT2: (0:5) 0 İLE 5 SATIR ARASI DEMEK ama df.iloc(0:2,0:3) bu iki boyutlu 0 2 satır arası 3. sutuna kadar 

