import numpy as np
"""
NumPy, Python için hızlı sayısal hesaplama kütüphanesidir. T
Temel amacı çok boyutlu diziler (ndarray) ve bu diziler üzerinde C hızında vektörize işlemler yapmaktır. 

ne işe yarar:
Büyük sayısal verileri verimli saklamak ve işlemek.

Matris / lineer cebir (çarpım, ters, özdeğer vb.).

İstatistiksel hesaplamalar (ortalama, standart sapma, vs.).

Rastgele sayı üretme (simülasyon, örnekleme).

Veri ön-işleme (dönüştürme, filtreleme, yeniden şekillendirme).

Bilimsel hesaplamalar, makine öğrenmesi ve görüntü işleme için temel yapı taşı.
"""

np.array([1,3,5,7,9]) #pyythondan dan numpy listesine çevirir 
np.arange(10,100,20) # 10 100 arasında 20 şet artan bir mupy list
np.zeros(10) # 10 sıfırlı
np.ones(10) # 1 lerden oluşuyor ve her bir eleman float değere sahibtir.
np.linspace(0,10,3) #  sonuç 0 5 10 üçe ayırır 5 desen 5 e ayırır
np.random.randint(0,10) # 0 ile 10 arasında rastgele sayı üretir 
np.reshape() # çok boyutlu dizi yaoar
#-------------------------------
numbers = np.array([[0,1,2],[3,4,5],[6,7,8]])
numbers[0] #0 1 2 
numbers[2,2] #[6,7,8] burdan 8 cevap 
numbers[:,1] # bu : demek bütün satırları seçmek tüm satırlardan 1. yani 1 4 7
numbers[:,0:2] # tüm satırlardan 0 ve 1 indexi alır 
numbers[-1,:] #son satırı alır [6,7,8]

#normalde bir referans yaptığımız zaman a = b  b deişlem yaprsak a da etkilenir çünü aynı bellek üzerinde tutuluyorlar
#ama a = b.copy() dersek b de yaptığımız işlemler a da işlem almaz çünkü ikisine farklı bellek tuulur 
#---------------------------------------------

np.vstack() # iki taane matrisi birletirir dikey olarak 
np.hstack() # iki tane matrisi bbirleştirir yatay olarak 
# bu tarz numpy değerleriyle karşılaştırma felan yapılabilir dizilerle result = numbers >= 50 (numbers bir ddizi) gibi tüm listeyi kontrol edebilirsin
