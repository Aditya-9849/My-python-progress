import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 300, 500, 400)
        self.button = QPushButton("Don't click Me", self)
        self.label = QLabel("Do not click the button", self)
        self.initUI()  # call the method to set up the UI

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # signal.connect(slot)
        # signal is emitted when the button is clicked, and it calls the on_click method (slot) 
        # to handle the event.

        self.label.setGeometry(150, 300, 250, 100)
        self.label.setStyleSheet("font-size: 20px;")

    def on_click(self):
        self.button.setText("Clicked!") # change the button text when clicked
        self.label.setText("You will die now") # change the label text when button is clicked
        self.button.setDisabled(True) # disable the button after click to prevent multiple clicks

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()