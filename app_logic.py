from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io


from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox

from bluesen_v4 import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI from bluesen_v3.py
        self.pushButton.clicked.connect(self.selectCoordinates) 
        self.pushButton_2.clicked.connect(self.goHome)
        self.lat = 40.7128
        self.lon = -74.0060

    def selectCoordinates(self):
        try:
            self.lat = float(self.lineEdit.text())
            self.lon = float(self.lineEdit_2.text())
            if not (-90 <= self.lat <= 90):
                raise ValueError("Latitude must be between -90 and 90")
            if not (-180 <= self.lon <= 180):
                raise ValueError("Longitude must be between -180 and 180")
            coordinate = (self.lat, self.lon)
            geoMap = folium.Map(zoom_start=11, location=coordinate)
            # Add a home icon to the map on selected corrdinates
            folium.Marker(
                location=[self.lat, self.lon], 
                popup="Marker Popup Text",
                icon=folium.Icon(icon="home", color="red")
            ).add_to(geoMap)
            data = io.BytesIO()
            geoMap.save(data, close_file=False)
            self.webView.setHtml(data.getvalue().decode())
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Invalid input", str(e))

    def goHome(self):
        coordinate = (self.lat, self.lon)
        geoMap = folium.Map(zoom_start=11, location=coordinate)
        folium.Marker(
                location=[self.lat, self.lon], 
                popup="Marker Popup Text",
                icon=folium.Icon(icon="home", color="red")
            ).add_to(geoMap)
        data = io.BytesIO()
        geoMap.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())
