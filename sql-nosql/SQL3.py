#UPDATE SQL’de var olan veriyi değiştirmek için kullanılır. Yani tabloya yeni satır eklemek değil, mevcut satırları güncellemek için
#DELETE SQL’de tablodan veri silmek için kullanılır.
import mysql.connector

connection = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "459145",
    database = "Student"
)
mycursor = connection.cursor()
#sql = "Update new_table Set Name='Volkan'" #tüüm tabloları volkan yapar
#sql = "Update new_table Set Name='Volkan' where name='Elif'" #name sutundaki elif yerleri volkan yapar

#sql = "Delete from new_table"  #tüm kayıtları siler 
#sql = "Delete from new_table where id=55" 
#sql = "Delete from new_table where name like '%an%'" #an yazan bütün satırları siler

mycursor.execute(sql)
try:
    connection.commit()
    #print(f'{mycursor.rowcount} tane kayıt Silindi.')
   #print(f'{mycursor.rowcount} tane kayıt yenilendi.')
except mysql.connector.Error as err:
    print("Hata:", err)

finally:
    connection.close()
    print("\nDatabase bağlantısı kapandı.")