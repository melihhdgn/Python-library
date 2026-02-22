from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox, QRadioButton, QComboBox, QSlider, QProgressBar, QTextEdit, QSpinBox
from PyQt6.QtCore import Qt
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt6 Widget Örnekleri")
        self.setGeometry(200, 150, 600, 500)
        
         # 1️⃣ QLabel → Sadece yazı veya bilgi gösterir
        self.label = QLabel("Merhaba! (QLabel)", self)
        self.label.move(20, 20)
        
        # 2️⃣ QPushButton → Tıklanabilir buton
        self.button = QPushButton("Butona Tıkla", self)
        self.button.move(20, 60)
        self.button.clicked.connect(lambda: print("Butona tıklandı!"))
        
        # 3️⃣ QLineEdit → Kullanıcıdan metin girişi almak
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 100)
        self.textbox.setPlaceholderText("Bir şey yaz...")
        
        # 4️⃣ QCheckBox → İşaret kutusu
        self.checkbox = QCheckBox("Seçeneği İşaretle", self)
        self.checkbox.move(20, 140)
        
        # 5️⃣ QRadioButton → Radyo butonu (tek seçim)
        self.radiobutton = QRadioButton("Seçenek 1", self)
        self.radiobutton.move(20, 180)
        
        # 6️⃣ QComboBox → Açılır menü
        self.combobox = QComboBox(self)
        self.combobox.addItems(["Seçenek A", "Seçenek B", "Seçenek C"])
        self.combobox.move(20, 220)
        
        # 7️⃣ QSlider → Kaydırma çubuğu
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.move(20, 260)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        
        # 8️⃣ QProgressBar → İlerleme çubuğu
        self.progress = QProgressBar(self)
        self.progress.move(20, 300)
        self.progress.setValue(50)
        
        # 9️⃣ QTextEdit → Uzun metin girişi
        self.textedit = QTextEdit(self)
        self.textedit.setPlaceholderText("Uzun metin buraya...")
        self.textedit.move(250, 20)
        self.textedit.resize(300, 100)
        
        # 🔟 QSpinBox → Sayı seçimi
        self.spinbox = QSpinBox(self)
        self.spinbox.move(250, 140)
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(10)
        
        self.show()

app = QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec())
