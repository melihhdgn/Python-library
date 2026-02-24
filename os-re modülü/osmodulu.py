import os 

# Python’un işletim sistemi ile iletişim kurmasını sağlar.
# Dosya/dizin işlemleri, sistem komutları çalıştırma, ortam değişkenlerine erişme gibi işlerde kullanılır.
result = dir(os) #hangi metodları var onu gösterir

os.chdir('C:\\') # BİR DOSYA kaydededtme yaparsan direk c de kaydedir.
os.mkdir("newfile") #.py dosyan nerdeyse oraya dosyayı kaydeder.
os.makedirs("newfile/yenidosya") # newfile içinde yeni dosya olışturur
os.listdir('C:\\') # C deki bütün dosyaları listeler.

result = os.stat("melih.py") # o dosya hakkındaki bilgilere ulaşırsın
result = result.st_size/1024 #boyut
datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma zamanı 
#atime olursa son erişilme, mtime olursa değiştirilme tarihi olur 

os.system("aımı.py") #istediğin dosyayı çalıştır
os.rename("aımı.py","aımıd.py") #klasor isim değişme

os.rmdir() #klasör silme ama alt dizinli olanı silmez alt dizin içi altındaki yaz sonra bunu
os.removedirs("yeniklasör/melih.py")

os.path.abspath("aımı.py") #dosya yolunu gösterir
os.path.dirname("c//hoome..") #buda konumdan dosya ismi bulur
os.path.dirname(os.path.abspath("aımı.py")) #bulunduğu klasörü gösterir
os.path.exists() #o dosya varmı yokmu
os.path.isdir() # klasörmü değilmi
os.path.isfile() #dosyamı değilmi
os.path.join("c,home,melih") #klasör yolu oluşturmak 
os.path.split() # yolları ayırır c,home,melih 
os.path.splitext("melih.py") #melih,.py diye ayırır uzantıysıyla ayırıyor.

""" 🔹 Öne çıkan özellikler:

os.getcwd() → Şu anki çalışma dizinini alır.

os.chdir(path) → Çalışma dizinini değiştirir.

os.listdir(path) → Bir dizindeki dosyaları listeler.

os.mkdir(name) / os.makedirs(path) → Dizin oluşturur.

os.remove(file) → Dosya siler.

os.rename(old, new) → Dosya veya klasörü yeniden adlandırır.

os.environ → Ortam değişkenlerine erişir.

"""



