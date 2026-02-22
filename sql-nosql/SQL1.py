#Server = Senin yönettiğin, sürekli açık duran mutfak.

#Serverless = İstediğinde sana yemek veren restoran (arkada mutfak var ama sen görmüyorsun, sadece kullandığın kadar ödüyorsun).
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "459145",
    database = "melihhh"
)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE melihhh") #yeni tablo oluşturma 

mycursor2 = mydb.cursor()
mycursor2.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #sutün oluşturma ama gerek yook workbenchte yaparsın """
"""
import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "459145",
    database = "schooldb"
)
"""


