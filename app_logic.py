from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QTimer
import folium
import io
import time
import random
import csv

from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox

from bluesen_v5 import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI from bluesen_v3.py
        self.pushButton.clicked.connect(self.selectCoordinates) 
        self.pushButton_2.clicked.connect(self.goHome)
        QTimer.singleShot(2000, lambda : self.loadDronePathFromCsv("test_tracks/cttn-6-170259UTC-QUAD_step1.csv"))

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

    def loadDronePathFromCsv(self, csv_path):
        """ Exrapolate lat/lon coordinates from CSV to send to the map."""
        try:
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    try:
                        if len(row) >= 2:
                            lat = float(row[2])
                            lon = float(row[3])

                            print(f"Pushing from CSV: {lat}, {lon}")
                            js_code = f"updateCoordinatesFromPython({lat}, {lon});"
                            self.webView.page().runJavaScript(js_code)
                            QTimer.singleShot(1500, lambda: self.webView.page().runJavaScript(
                                "JSON.stringify(coordinates)",
                                lambda result: print("JS Coordinates (after delay):", result)
                            ))
                    except ValueError:
                        print(f"Invalid coordinates: {row}")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self, "File Not Found", f"Could not open {csv_path}")

