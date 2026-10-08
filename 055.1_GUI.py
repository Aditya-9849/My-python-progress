import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow): #this class inherits from QMainWindow 
    def __init__(self):
        super().__init__() # this calls the constructor of the parent class QMainWindow
        self.setWindowTitle("My first GUI")
        self.setGeometry(300, 300, 400, 300) #(x, y, width, height)
        self.setWindowIcon(QIcon("055.2_icon.png"))  # Set your icon path here

def main():
    app = QApplication(sys.argv)  # creates an instance of the QApplication class,
    # which is necessary for any PyQt5 application, must be created before any GUI elements.
    window = MainWindow() #creates an instance of the MainWindow class, which is our main window 
    window.show()         # makes the main window visible on the screen.
    
    sys.exit(app.exec_()) 
'''Starts the application's event loop with app.exec_() — this keeps the app running, 
listening for events (clicks, key presses, etc.) until the window is closed. 
app.exec_() returns an exit code when the loop ends,
and sys.exit() passes that code back to the OS, ensuring a clean shutdown.'''

if __name__ == "__main__":
    main()