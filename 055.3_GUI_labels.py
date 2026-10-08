# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #for alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.setGeometry(200,200,350,450)
        label = QLabel(parent = self, text ="Hello") #QLabel("Hello", self) - without keywords, base method
        label.setFont(QFont("Arial", 40)) # ("font", font size)
        label.setGeometry(0,0,350,100)
        label.setStyleSheet("color : #08d6e4;"
                            "background-color : #0d1f14;"
                            "font-weight : bold;"
                            "font-style : italic;"
                            "text-decoration : underline") # color name or code must end with ;
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) # vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # vertically center
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter) # horizontally center
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) # vertically top, horizontally center 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()