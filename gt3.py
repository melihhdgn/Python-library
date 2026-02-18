"""
🎛️ ComboBox nedir?

ComboBox, kullanıcıya birden fazla seçenek sunan ama hepsini aynı anda göstermeyip, açılır bir liste (dropdown) şeklinde gösteren bir bileşendir.

Yani:

Kullanıcı tıklamadan önce sadece bir kutu görür,
tıklayınca aşağı doğru açılır ve seçeneklerden birini seçer.

🎨 Gerçek hayattan benzetme:

Bir web sitesinde ülke seçimi yaparken düşün:

Türkiye

Almanya

Fransa

ABD

Hepsi bir listede ama sen tıklayana kadar sadece “Bir ülke seçin” yazıyor.
Tıklayınca açılıyor ve seçim yapıyorsun.
İşte bu bir ComboBox.

"""
#DATE VE TİME 
"""

import sys                                # Uygulama çalıştırmak için
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QDateTimeEdit, QPushButton, QLabel
)
from PyQt6.QtCore import QDateTime        # Tarih-saat tipi

app = QApplication(sys.argv)              # PyQt uygulamasını başlat

window = QWidget()                        # Ana pencere
window.setWindowTitle("Date Time")        # Pencere başlığı

layout = QVBoxLayout()                    # Dikey yerleşim
window.setLayout(layout)

datetime_edit = QDateTimeEdit()           # Tarih + saat seçici
datetime_edit.setDateTime(
    QDateTime.currentDateTime()
)                                         # Varsayılan: şu an
datetime_edit.setCalendarPopup(True)      # Takvim açılır olsun

label = QLabel("Seçilen tarih")           # Sonucu gösterecek yazı

button = QPushButton("Al")                # Buton

def get_datetime():                       # Butona basınca çalışır
    dt = datetime_edit.dateTime()         # Seçilen tarih-saat
    text = dt.toString("dd.MM.yyyy HH:mm")# String'e çevir
    label.setText(text)                   # Label'a yaz

button.clicked.connect(get_datetime)      # Buton → fonksiyon

layout.addWidget(datetime_edit)           # Arayüze ekle
layout.addWidget(button)
layout.addWidget(label)

window.show()                             # Pencereyi göster
sys.exit(app.exec())                      # Uygulamayı çalıştır

🧠 KISA ÖZET
QDateTimeEdit → kullanıcı tarih/saat seçer

.dateTime() → QDateTime alırsın

.toString() → saklanabilir string olur

"""
#MessageBox = kullanıcıyla konuşma penceresi

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView
from PyQt6.QtCore import QStringListModel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("ListView Örneği")

layout = QVBoxLayout()
window.setLayout(layout)

model = QStringListModel()
model.setStringList(["Ali", "Ayşe", "Mehmet"])

list_view = QListView()
list_view.setModel(model)

layout.addWidget(list_view)

window.show()
sys.exit(app.exec())

# ListView = çok sayıda veriyi düzenli, hızlı ve profesyonel şekilde göstermek için vardır.
#ListView, büyük ve değişken veriyi kullanıcıya takılmadan göstermek için vardır. kısacası arkada bir veri yapısı yok sadece arayüz gösterimi var .

#📌 Birden fazla bilgi varsa → TableView kütüpü aynı mantık üstekiyle 