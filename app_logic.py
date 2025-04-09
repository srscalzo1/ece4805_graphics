from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io
import time
import random

from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox

from bluesen_v4 import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI from bluesen_v3.py
        self.pushButton.clicked.connect(self.selectCoordinates) 
        self.pushButton_2.clicked.connect(self.goHome)

    def selectCoordinates(self):
        try:
            self.lat = float(self.lineEdit.text())
            self.lon = float(self.lineEdit_2.text())
            if not (-90 <= self.lat <= 90):
                raise ValueError("Latitude must be between -90 and 90")
            if not (-180 <= self.lon <= 180):
                raise ValueError("Longitude must be between -180 and 180")

            # Call the JavaScript function to select coordinates
            js_code = f"""
                selectCoordinates({self.lat}, {self.lon});
            """
            self.webView.page().runJavaScript(js_code)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Invalid input", str(e))


    # Call the JavaScript function to go home
    def goHome(self):
        js_code = f"""
            goHome({self.lat}, {self.lon});
        """
        self.webView.page().runJavaScript(js_code)

    # Todo: update this to parse a given csv file that contains data. Send that data to java script
