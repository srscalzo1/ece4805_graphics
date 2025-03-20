import sys
from PyQt5 import QtWidgets
from app_logic import AppWindow

def main():
    app = QtWidgets.QApplication(sys.argv)  # Create the application object
    MainWindow = AppWindow()
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application event loop

if __name__ == "__main__":
    main()