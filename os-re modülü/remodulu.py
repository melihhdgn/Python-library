import re
"""Düzenli ifadeler, metin içinde belli bir deseni (pattern) aramak, 
kontrol etmek veya değiştirmek için kullanılan güçlü bir araçtır.
"""
result = dir(re) #kullanacağımız metodlar

str = "Melih Doğan Turgut Özal Üniversitesinde Okuyor | 21 yaşında 2 projesi var"

result = re.findall("Melih",str) #str içinde melihi ara len(result) yaparsan kaç tane olduğunu bulursun
result = re.split("T", str) #büyük T görünce bölünür
result = re.sub("M","C",str)  #strdeki M leri C ile değiş

result = re.search("melih",str) #pythonda melihi ara farkı 0 ile 10 arasında buldum gibi der
result = result.span() #melihin konumu
#result.start veya end kaçtan başladı kaçta bitti söyle

result = re.findall("[abc]", str)  
# 'a', 'b', veya 'c' karakterlerini tek tek arar, kaç tane varsa döner

result = re.findall("[a-e]", str)  
# 'a'dan 'e'ye kadar olan karakterleri arar (a,b,c,d,e)

result = re.findall("[0-2]", str)  
# '0', '1', veya '2' rakamlarını arar

result = re.findall("[0-29]", str)  
# '0', '1', '2', ve '9' rakamlarını arar (9 tek başına sabittir)

result = re.findall("[^mdf]", str)  
# 'm', 'd', 'f' dışındaki tüm karakterleri arar

result = re.findall("[abc]", str)  
# 'a', 'b', veya 'c' karakterlerini arar (örnek: "abcd" içinde sadece a,b,c döner)

result = re.findall("[^a]", str)  
# 'a' olmayan tüm karakterleri arar

result = re.findall("a$", str)  
# Metnin sonunda 'a' karakteri var mı diye kontrol eder

result = re.findall(r"ab+", str)  
# 'a' harfinden sonra en az 1 tane 'b' olanları bulur (ab, abb, abbb gibi)

result = re.findall(r"ab*", str)  
# 'a' harfinden sonra 0 veya daha fazla 'b' olanları bulur (a, ab, abb, abbb gibi)

result = re.findall(r"ab?", str)  
# 'a' harfinden sonra 0 veya 1 tane 'b' olanları bulur (a veya ab)

result = re.findall("a{2}", str)  
# Ardışık 2 tane 'a' arar (aa)

result = re.findall("a|b", str)  
# 'a' veya 'b' karakterlerinden biri var mı diye arar

result = re.findall("(a|b|c)xz", str)  
# 'a', 'b' veya 'c' ile başlayıp ardından 'x' ve 'z' gelenleri bulur (axz, bxz, cxz)

result = re.findall(r"\A", str)  
# Metnin başını gösterir (başlangıç kontrolü)

result = re.findall(r"\Z", str)  
# Metnin sonunu gösterir (bitiş kontrolü)

result = re.findall(r"\bthe", str)  
# 'the' kelimesinin başındaki kelime sınırını arar (the kelimesi kelime başında)

result = re.findall(r"the\b", str)  
# 'the' kelimesinin sonundaki kelime sınırını arar (the kelimesi kelime sonunda)

result = re.findall(r"\B", str)  
# Kelime sınırı olmayan yerleri bulur

result = re.findall(r"\d", str)  
# Herhangi bir rakam (0-9) arar

result = re.findall(r"\D", str)  
# Rakam olmayan karakterleri arar

result = re.findall(r"\s", str)  
# Boşluk karakterlerini arar (space, tab, newline)

result = re.findall(r"\S", str)  
# Boşluk olmayan karakterleri arar

result = re.findall(r"\w", str)  
# Harf, rakam veya alt çizgi (_) karakterlerini arar

result = re.findall(r"\W", str)  
# Harf, rakam veya alt çizgi olmayan karakterleri arar





print(result) 

