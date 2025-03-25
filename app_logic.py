from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io

from PyQt5.QtWidgets import QMainWindow

from bluesen_v3 import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI from bluesen_v3.py
        self.pushButton.clicked.connect(self.updateMap)  # Override method

    def updateMap(self):
        try:
            coordinate = (float(self.lineEdit.text()), float(self.lineEdit_2.text()))
            geoMap = folium.Map(zoom_start=11, location=coordinate)
            data = io.BytesIO()
            geoMap.save(data, close_file=False)
            self.webView.setHtml(data.getvalue().decode())
        except ValueError:
            print("Invalid input: Please enter numeric values for coordinates.")