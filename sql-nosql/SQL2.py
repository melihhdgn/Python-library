#İNSERT SORGUSU 

#SQL’de INSERT komutu, bir tabloya yeni veri eklemek için kullanılır.
"""
import mysql.connector

def insertprduct():
    connection = mysql.connector.connect(host="localhost", user="root", password="459145",database="node-app")
    cursor = connection.cursor() #sql ile iletişim kısmı hep olmalı

    sql = "INSERT INTO new_table(name,surname,yas) VALUES (%s,%s,%s)"
    values = ("Semih","Doğan", 34)
  
    cursor.execute(sql,values)
    connection.commit()
    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("DATABASE BAĞLANTISI KAPANDI")
insertprduct() """

#İnsert uygulama 

import mysql.connector

connection = mysql.connector.connect (
     host = "localhost",
     user = "root",
     password = "459145",
     database = "Student"
)

mycursor = connection.cursor()

sql = "INSERT INTO new_table(StudentNumber,Name,Surname,Gender) VALUES (%s,%s,%s,%s)"

ogrenciler = [
    [1, "Ali", "Yılmaz", "M"],
    [2, "Ayşe", "Demir", "F"],
    [3, "Mehmet", "Kaya", "M"],
    [4, "Elif", "Çelik", "F"],
    [5, "Ahmet", "Şahin", "M"],
    [6, "Zeynep", "Koç", "F"],
    [7, "Hasan", "Özkan", "M"],
    [8, "Fatma", "Arslan", "F"],
    [9, "Yusuf", "Polat", "M"],
    [10, "Hatice", "Kaplan", "F"],
    [11, "Murat", "Aydın", "M"],
    [12, "Emine", "Tekin", "F"],
    [13, "Okan", "Güneş", "M"],
    [14, "Derya", "Bulut", "F"],
    [15, "Serkan", "Karaca", "M"],
    [16, "Merve", "Bozkurt", "F"],
    [17, "Hakan", "Taş", "M"],
    [18, "Gamze", "Korkmaz", "F"],
    [19, "Can", "Erdem", "M"],
    [20, "Selin", "Yavuz", "F"],
    [21, "Onur", "Tuncer", "M"],
    [22, "Ceren", "Acar", "F"],
    [23, "Kaan", "Sezer", "M"],
    [24, "Ezgi", "Bilgin", "F"],
    [25, "Burak", "Topal", "M"],
    [26, "İrem", "Deniz", "F"],
    [27, "Gökhan", "Ekinci", "M"],
    [28, "Sevgi", "Öztürk", "F"],
    [29, "Taylan", "Uçar", "M"],
    [30, "Ebru", "Aslan", "F"],
    [31, "Furkan", "Kurt", "M"],
    [32, "Melisa", "Aksoy", "F"],
    [33, "Berk", "Tunç", "M"],
    [34, "Seda", "Ersoy", "F"],
    [35, "Tolga", "Baran", "M"],
    [36, "Esra", "Sağlam", "F"],
    [37, "Engin", "Dinç", "M"],
    [38, "Deniz", "Torun", "F"],
    [39, "Volkan", "İlhan", "M"],
    [40, "Gül", "Aktaş", "F"],
    [41, "Barış", "Şen", "M"],
    [42, "Pelin", "Özdemir", "F"],
    [43, "Efe", "Yıldırım", "M"],
    [44, "Nisan", "Çakır", "F"]
]


mycursor = connection.cursor()

try:
    # 1 Tüm kayıtları oku
    """ 
    mycursor.execute("SELECT * FROM new_table")
    tum_kayitlar = mycursor.fetchall()
    print("Tablodaki tüm kayıtlar:")
    for kayit in tum_kayitlar:
        print(f'ID:{kayit[0]} StudentNumber:{kayit[1]} Name:{kayit[2]} Surname:{kayit[3]} Gender:{kayit[4]}')"""
    

    # 2 Where komutu veri filtreleme
    """
    #mycursor.execute("SELECT * FROM new_table WHERE Name='Volkan'")
    #mycursor.execute("SELECT * FROM new_table WHERE Name='Volkan' and StudentNumber=39 ")  #nosu 39 ve volkan isimliyi çağırır or opertörüde kullanılır
    mycursor.execute("SELECT * FROM new_table WHERE Name LIKE '%an%' ") #NAME Alanında an geçen kayıtları listleer 
    kayit = mycursor.fetchall()  # tek satır al
    if kayit:
    #for kayit in kayit: #fetchall yapıp tüm hepsini yazdırabilirsin tekbir yazdırmak harici 
        print(f'Name: {kayit[1]} Surname: {kayit[2]} Gender: {kayit[3]}')
    else:
        print("\n kayıt bulunamadı.")"""
    
     #3 Orderby  ORDER BY SQL’in sıralama yapmak için kullanılan komutudur
    """
    mycursor.execute("SELECT * FROM new_table Order By StudentNumber DESC ") # ASC artan DESC Azalan demek student number dan sonra eklersen
    kayit = mycursor.fetchall()  # tek satır al
    #if kayit:
    for kayit in kayit: #fetchall yapıp tüm hepsini yazdırabilirsin tekbir yazdırmak harici 
        print(f'Name: {kayit[1]} Surname: {kayit[2]} Gender: {kayit[3]}')
    #else:
        #print("\n kayıt bulunamadı.")
"""

except mysql.connector.Error as err:
    print("Hata:", err)

finally:
    connection.close()
    print("\nDatabase bağlantısı kapandı.")


#AGGREDE FONKLARI 
"""
COUNT	Satır sayısını verir	SSELECT COUNT(*) FROM new_table;
SUM	Sayısal sütunları toplar	SELECT SUM(StudentNumber) FROM new_table;
AVG	Sayısal sütunların ortalamasını alır	SELECT AVG(StudentNumber) FROM new_table;
MIN	En küçük değeri verir	SELECT MIN(StudentNumber) FROM new_table;
MAX	En büyük değeri verir	SELECT MAX(StudentNumber) FROM new_table; """