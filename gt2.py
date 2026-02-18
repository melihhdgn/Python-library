"""
🧩 Qt Designer Nedir?

Qt Designer, PyQt6 arayüzlerini görsel olarak tasarlamak için kullanılan bir araçtır.

Kod yazmadan buton, label, text box gibi bileşenleri sürükle-bırak yöntemiyle yerleştirmemizi sağlar.

Tasarlanan arayüz .ui uzantılı bir dosya olarak kaydedilir ve Python koduna dönüştürülerek PyQt6 projelerinde kullanılır.

🔧 Avantajı: Kodla tek tek widget eklemek yerine, tasarımı görsel olarak hızlıca hazırlarsın.

📐 Layout (Yerleşim) Nedir?

Layout’lar, arayüz elemanlarının ekranda düzenli ve esnek şekilde yerleşmesini sağlar.

Pencere yeniden boyutlandırıldığında bile elemanların düzgün kalmasını garantiler.

📦 Temel Layout Türleri:

Horizontal Layout (QHBoxLayout): Elemanları yatayda (yan yana) dizer.

Vertical Layout (QVBoxLayout): Elemanları dikeyde (alt alta) dizer.

Grid Layout (QGridLayout): Hücre sistemiyle tablo gibi yerleştirir.

Form Layout (QFormLayout): Etiket–girdi çiftlerini düzenli biçimde yerleştirir.

"""

"""
🎛️ Radio Button nedir?

“Radio button” (ya da Türkçesiyle “seçenek düğmesi”), kullanıcıya birden fazla seçenek sunup sadece bir tanesini seçtirmek için kullanılır.

Yani mantığı şudur:

“Birden fazla seçenek var ama sadece birini işaretleyebilirsin.”
"""
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel
import sys

class RadioOrnek(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button Örneği")
        self.resize(300, 150)

        # Dikey düzen oluştur
        layout = QVBoxLayout()

        # Label (seçilen rengi göstermek için)
        self.label = QLabel("Bir renk seç:")
        layout.addWidget(self.label)

        # Radio butonlar
        self.red = QRadioButton("Kırmızı")
        self.green = QRadioButton("Yeşil")
        self.blue = QRadioButton("Mavi")

        # Hepsini layout’a ekle
        layout.addWidget(self.red)
        layout.addWidget(self.green)
        layout.addWidget(self.blue)

        # Radio butonlara tıklanınca çalışacak fonksiyon
        self.red.toggled.connect(self.renk_degisti)
        self.green.toggled.connect(self.renk_degisti)
        self.blue.toggled.connect(self.renk_degisti)

        self.setLayout(layout)

    def renk_degisti(self):
        if self.red.isChecked():
            self.label.setText("Seçilen renk: Kırmızı")
        elif self.green.isChecked():
            self.label.setText("Seçilen renk: Yeşil")
        elif self.blue.isChecked():
            self.label.setText("Seçilen renk: Mavi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = RadioOrnek()
    pencere.show()
    sys.exit(app.exec())
