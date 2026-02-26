"""BeautifulSoup Python’da HTML ve XML verilerini kolayca parse (çözümlemek) için kullanılan bir kütüphane.
En çok web scraping (yani bir web sitesinden veri çekme) işlerinde kullanılır.

📌 Temel Mantığı
Bir web sayfasından HTML kodunu alırsın (genelde requests ile).

BeautifulSoup bu HTML’yi ağaç yapısına çevirir.

Sen de bu ağaçta etiketleri, sınıfları, id’leri kolayca bulursun.""" 


html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>Örnek Web Sayfası</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Hoş Geldiniz!</h1>
    <p>Bu basit bir HTML sayfasıdır.</p>

    <h2>Hakkımızda</h2>
    <p>Biz yazılım öğreniyoruz ve kodlamaya yeni başladık.</p>

    <h3>Yaptıklarımız</h3>
    <ul>
        <li>Python öğrenmek</li>
        <li>Web geliştirme</li>
        <li>API kullanmak</li>
    </ul>

    <h3>İletişim</h3>
    <p>Bize <a href="mailto:ornek@mail.com">email</a> gönderebilirsiniz.</p>

    <img src="https://via.placeholder.com/150" alt="Örnek Resim">

    <p><strong>Teşekkürler!</strong></p>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")   #parse etmek anlamlandırmak veriyi HTML’i Python’un anlayabileceği bir yapıya çevirir
result = soup.prettify()   #HTML veya XML yapısını daha okunabilir, düzgün ve girintili (indent edilmiş) şekilde string olarak döner.
result = soup.title #sadce tittle çeker head veya body dersen sadece oraları yazar
result = soup.title.string #<m>  içindeki m yi yazdırır yani kısacası soup içeride bişeyleri çekme denir. 
result = soup.find_all('m') #sayfadaki bütün m etiketlerini getirir [0] [1] diye yazılabilir.
result = soup.div.findChildren() #div altındaki tüm etiketleri gösterir 
print(result)
