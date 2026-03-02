
#döngüsüz matematik 

import numpy as np
"""
result = np.array([10,15,30,45,60])
result2 = np.arange(5,15)
result3 = np.arange(50,100,5)
result4 = np.zeros(4)
result5 = np.linspace(0,100,5)
result6 = np.random.randint(10,30,5)
result7 = np.random.uniform(-1,1,10) """
#--------------
"""
result8 = np.random.randint(10,50,(3,3)) #10 50 arasında 3x3 matris
satir_toplam = matris.sum(axis=1) #dizinin satırlarını toplar
sutun_toplam = matris.sum(axis=0) #dikeylerni toplar

axis hangi yönde işlem yapılacağını söyler:
axis=0 → dikey eksen, yani sütunlar boyunca işlem yapar.
axis=1 → yatay eksen, yani satırlar boyunca işlem yapar.
"""
#-------------------------------
"""
result8 = np.random.randint(10,50,(3,3))
toplam = 0
for i in range(3):
    for k in range(3):   #tüm boyutluyu dizinin elemanlarını toplar
        toplam += result8[i][k]

print(result8)
print(toplam) """
#----------------------
"""
#üretilen matrisin en büyük değeri en küçük değeri ve ortalaması
result8 = np.random.randint(10,50,(3,3))
print(result8)
en_kucuk = result8[0][0]
en_buyuk = result8[0][0]
toplam = 0
for i in range(3):
    for k in range(3):
        if en_kucuk >= result8[i][k]:
            en_kucuk = result8[i][k]
        if en_buyuk <= result8[i][k]:
            en_buyuk = result8[i][k]
        toplam += result8[i][k] / len(result8)
        
print("En büyük sayı:",en_buyuk)
print("En küçük sayı:",en_kucuk) 
print("Dizinin ortalaması:",toplam) """ #bunla ugrasmak yerine min max mean kullanabilirsin





