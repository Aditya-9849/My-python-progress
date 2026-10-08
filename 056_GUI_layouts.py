import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout)

'''normally we cant add a layout manager to mainwindow object cuz mainwindow have
specific design and layout, so we create a generic widget and add layout manager to it, 
then we add that widget to mainwindow object'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts")
        self.setGeometry(200, 200, 400, 300)
        self.initUI()  # call the method to set up the UI

    def initUI(self):  # to keep things organised
        central_widget = QWidget()  # create a generic widget
        self.setCentralWidget(central_widget)

        label1 = QLabel("Label 1", self) # self is not needed here, but we can use it
        label2 = QLabel("Label 2", self)
        label3 = QLabel("Label 3", self)
        label4 = QLabel("Label 4", self)
        label5 = QLabel("Label 5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: purple;")

        vbox = QVBoxLayout()  # create a vertical box layout
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

        # use QHBoxLayout for horizontal layout and replace vbox with hbox
        # we can also use QGridLayout for grid layout, 
        # but we need to specify row and column for each widget like this:
        # grid = QGridLayout()
        # grid.addWidget(label1, 0, 0)  # row 0, column 0
        # grid.addWidget(label2, 0, 1)  # row 0, column 1
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()