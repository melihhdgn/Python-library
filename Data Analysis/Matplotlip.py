#Matplotlib, Python’da grafik çizmek için kullanılan en popüler kütüphanelerden biridiR.
#matplotlip.org sayfasında bütün kullannımları yazıoyr
import matplotlib
matplotlib.use("TkAgg")   # grafik penceresi açmak için
import matplotlib.pyplot as plt
import numpy as np 
"""
x = [1,2,3,4,5]
y = [1,4,5,6,3]
plt.plot(x,y) #grafik çizer
plt.axis([0,10,1,20]) #x ekseni 0 ile 10 y ekseni 1 ile 20 arasında geçerli
plt.title("Melih") #genel ismi
plt.xlabel("x") 
plt.ylabel("y")
plt.plot(x,y,color="red",linewidth="5") # color renk linewidth kalınlık
plt.legend() # grafikta hangi çizginin neyi temsil ettiğini göstermek için kullanılır.
plt.subplots(2) # bir ekranda 2 grafik yazdırır 
plt.show()

"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="yellow")   #1 karede 4 grafik böyle yazılır
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="purple")
plt.show()
"""
#----------------------------------

#MATPLOTLİP İLE FİGURE OLUŞTURMA
"""
x = np.linspace(-10,9,20)
y = x ** 2
z = x ** 3

figure = plt.figure()
axes_x = figure.add_axes([0.1,0.1,0.2,0.2]) #grafiğin konumunu belirler 
axes_x.plot(x,y,"b")
# 2 tane grafik oluşturu 1 axes üzerinnden 2 grafik çizebilirsin
#figure = sayfa demek axes çizilen grafik bölgesi demek
#figure ninde boyutuyla oybayabiliriz küçültüp büyütebilirz yanı sayfayı
#diyelim subsplot ile tek figurede 4 tane grafik var onlarında konumunu istdiğimiz gibi ayarlayabiliriz 

plt.show()
"""

#----------------------------------------------
#MATPLOTLİP GRAFİK TÜRLERİ 
"""
#STACK PLOT
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,23,7,9]
oyuncu2 = [1,11,2,33,6]
oyuncu3 = [2,13,83,56,76]

plt.plot([],[],color="y",label = "oyuncu1")
plt.plot([],[],color="r",label = "oyuncu2")
plt.plot([],[],color="g",label = "oyuncu3")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","g"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("gol sayısı")
plt.ylabel("yıl")
plt.legend() #sağda solda yazıyoya oyuncu1 kırmızı çizgi oyuncu mavi çizgi o bu yapıyor

plt.show()"""
"""
#PASTA GRAFİĞİ
goal_types = "Penaltı", "Kaleye atılan Şut", "Serbest vuruş"
goals = [12,34,122]
colors = ["y", "r", "g"]
plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=[0.01,0.2,0.04]) #shadow gölgelendirme yapar , explode ayırır dilimleri autopct= ise yüzdelik olarak gösterir

plt.show()"""


#BAR GRAFİĞİ(sutün)

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,80,90,12],label="BMW"width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[60,20,70,120,8],label="AUDİ"width=.5)

plt.legend()
plt.xlabel("GÜN")
plt.ylabel("Mesafe(km)")
plt.title("ARAÇ BİLGİSİ")
plt.show()

#bide histogram var onada bakarsın işine lazım olrusa 