import sys
from PyQt5 import QtWidgets
from bluesen_v3 import Ui_MainWindow  # Import your generated UI class

def main():
    app = QtWidgets.QApplication(sys.argv)  # Create the application object
    MainWindow = QtWidgets.QMainWindow()  # Create the main window
    ui = Ui_MainWindow()  # Instantiate the UI class
    ui.setupUi(MainWindow)  # Set up the UI on the main window
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application event loop

if __name__ == "__main__":
    main()