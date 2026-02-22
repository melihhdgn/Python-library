"""
SQL veritabanlarında (örneğin MySQL, PostgreSQL) veriler tablolarda, satır–sütun şeklinde tutulur.
Ama NoSQL veritabanlarında veri daha esnek biçimlerde saklanır:

JSON belgeleri

Anahtar–değer çiftleri

Grafik yapıları

Kolon bazlı sistemler

Bu sayede özellikle büyük veri (Big Data), gerçek zamanlı analiz ve ölçeklenebilir uygulamalarda çok avantajlıdır.
"""
"""
import pymongo 

myclient = pymongo.MongoClient("mongodb://localhost:27017") #Bu satır seni MongoDB sunucusuna bağlar
mydb = myclient["melih"] #burada “melih” adlı veritabanını seçiyorsun. Eğer o isimde bir veritabanı yoksa — ilk veri eklediğinde otomatik oluşturulur.
print(myclient.list_database_names()) #sunucudaki veri tabanlarını listeler 
"""
"""
import pymongo

# 1️⃣ MongoDB sunucusuna bağlan
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 2️⃣ 'node-app' adlı veritabanını seç (yoksa otomatik oluşur)
mydb = myclient["node-app"]

# 3️⃣ 'app' adlı koleksiyonu seç (yoksa yine otomatik oluşur)
mycollection = mydb["app"]

# 4️⃣ Eklenecek belge (JSON benzeri dict)
product = {"name": "Samsung S5", "price": 2000}

# 5️⃣ Veriyi koleksiyona ekle
result = mycollection.insert_one(product)

# 6️⃣ MongoDB’nin oluşturduğu benzersiz _id’yi yazdır
print("✅ Veri eklendi, id:", result.inserted_id)
"""


import pymongo


# 1️⃣ MongoDB sunucusuna bağlan
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["node-app"]
mycollection = mydb["app"]


#VERİ EKLEME İNSERT SORUGUSU
""" 
productlist = [
    {"name": "Samsung S6", "price": 3000, "description":"iyi telefon"}, #en önemli özelliği bi kısımda yok diğer taaflarda var 
    {"name": "Samsung S7", "price": 5000},
    {"name": "Samsung S8", "price": 6000},
    {"name": "Samsung S9", "price": 7000},
    {"name": "Samsung S1", "price": 8000},         #coklu veri ekleme
    {"name": "Samsung S2", "price": 9000},
    {"name": "Samsung S3", "price": 10000},
]
result = mycollection.insert_many(productlist)
#print(result.inserted_ids) """


#FİND SORGUSU
"""
result = mycollection.find_one() #ilk gördüğü 1 tane kaydı getirir 
for i in mycollection.find(): #tüm kayıtları yazdırır burda filtreleme yapabilirsin sutunlar arasında
    print(i)"""


#FİLTER SORGUSU FİLTRELEME
"""
filter = {"name":"Samsung s5"}
for i in mycollection.find(filter):
    print(i) """
#NOT: ıd üzerindende işlem yapılır Objeckıd importla öyyle yap 
#asşağıdaki sadece samsung s5 ve s6 olanları çeker $in bunun gibi çok fazla operotor var
"""
result = mycollection.find({
    "name": {
        "$in" : ["Samsung S5", "Samsung S6"]
    }
}) 
print(result)

for i in result:
    print(i) """ 


#SORT SORGUSU 
"""
result = mycollection.find().sort("name", 1) #1 i -1 yaz kaldır küçükten büyüğe 1 ile büyüken küçüğe
for i in result:
    print(i)
    """


#UPDATE SORGUSU (KAYIT GÜNCELLEME)
"""
mycollection.update_one( #ikitnae kayıt güncellediğinde update_many ile yapcan
    {"name": "Samsung S5"},
    {"$set": {
        "name" : "Iphone 6"
    }}
    )
for i in mycollection.find():
    print(i)"""


#DELETE SORGUSU
for i in mycollection.find():
    print(i)

print("*"*50)

mycollection.delete_one({"name":"Samsung S6"}) #many dersen hepsini siler bu birini

for i in mycollection.find():
    print(i)






