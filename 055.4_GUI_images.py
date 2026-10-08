#  in this project, we r going to add images to our GUI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

'''sys is needed so the app can exit cleanly and hand control back to the OS.
QApplication — every PyQt5 app needs exactly one of these. It manages the event loop, 
              settings, and app-wide resources.
QMainWindow — the base class for a normal desktop window (title bar, resizable frame, etc.). 
              Your custom window class inherits from it.
QLabel — normally used for text, but it's also PyQt's go-to widget for displaying images. 
         A label can hold either text or a pixmap.
QPixmap — represents an actual image loaded into memory, ready to be drawn on screen.'''

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,300)

        label = QLabel(self)
        label.setGeometry(0,0,500,300)

        pixmap = QPixmap("055.5_car.png") #created a pixmap variable to store img location
        label.setPixmap(pixmap) # set the label to show the image instead of text 
        label.setScaledContents(True) # label show a img to original size without scaling
                                    # this line tells to fill the img exactly as said

def main():
    app = QApplication(sys.argv) # starts the application, must created before any widgets
    window = Mainwindow() # builds custom window, runs the code from above
    window.show() # window is invisible until called them to show up by .show()
    sys.exit(app.exec_()) # app.exec_() starts and keep it running until closed
                        # sys.exit() makes sure the exit code goes to the OS properly

if __name__=="__main__":
    main()

'''                 QUICK SUMMARY:
create app -> build a window -> put a label inside it -> load img into the label ->
stretch the img to fill inside the label -> show the window -> run the event loop'''

'''            IMPORTANT POINTS TO REMEMBER
app = QApplication(sys.argv)
This has to be the first thing you do in any PyQt5 program, before creating any widgets or windows. 
QApplication sets up the whole GUI environment — fonts, screen info, event handling system, etc. 
If you try to create a QLabel or QMainWindow before this line exists, it'll crash.

sys.exit(app.exec_())
This is the trickiest line, so let's break it into two parts:
1. app.exec_() starts the event loop. This is the core of any GUI program — it's an infinite loop 
    running in the background that continuously listens for events: mouse clicks, key presses, 
    window resizes, close button clicks, etc. Without this, your window would flash on screen 
    for a split second and the script would immediately end, because there'd be nothing keeping 
    the program alive to listen for input. app.exec_() blocks (pauses) the rest of your code right here, 
    and keeps running until the user closes the window. When the window is closed, 
    app.exec_() returns an exit status code (an integer — 0 typically means "closed normally,
    " non-zero means some error happened).
    
2. sys.exit(...) takes that code and passes it back to the operating system as the program's exit status. 
    This matters mostly for things like scripts or shell pipelines that might check "did this program 
    exit successfully?"'''