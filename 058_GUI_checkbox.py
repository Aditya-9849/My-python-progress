import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBoxes")
        self.setGeometry(200, 300, 350, 350)
        self.checkbox = QCheckBox("I like pizza",self) # 2nd argument here says that this lives inside
                                                       # parent Mainwindow because parenting matters in Qt
        self.initUI() #custom method to organise code

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size : 30px;" \
        "font-family : Arial;")
        self.checkbox.setChecked(False) # initial state of checkbox is unchecked
        self.checkbox.stateChanged.connect(self.checkbox_changed) # signal.connect(slot)

# 19th is important line, it is PyQt5 "signal and slot" mechanism, it automatically fires when there is signal
# .connect() wires the signal to self.checkbox_changed and runs that method

    def checkbox_changed(self, state):
        if state == Qt.Checked:  # here Qt.checked is a constant with value = 2
                                 # if checkbox is ticked, "state" will return 2
            print("You like pizza")
        else:                    # if not ticked, it will return 0
            print("You don't like pizza")

def main():    # memorise this whole part no other way
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()