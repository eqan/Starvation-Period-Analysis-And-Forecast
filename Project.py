import pandas as pd
import numpy as np
import seaborn as sns
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidget,  QTableWidgetItem, qApp, QAction, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
import sys


# Data Variables
dataSkipped = pd.read_csv(r'./Project-Dataset.csv', skiprows=range(1,47))
dataWhole = pd.read_csv(r'./Project-Dataset.csv')
# Setting plot size
# plt.rcParams['figure.figsize'] = 13, 5

# Basic configuration for multiple-bar chart
n=len(dataSkipped)
r = np.arange(n)
width = 0.2

def clearContentArea(layout):
        for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setParent(None)

# Analysis Related Functionalities
## Start
class analysisForConsumptionProductionAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(1000, 100), dpi=95)
        super().__init__(fig)
        self.setParent(parent)
        """ 
        Matplotlib Script
        """
        self.ax.bar(r, (dataSkipped["Wheat Consumption Growth Rate"] + dataSkipped["Barley Consumption Growth Rate"] + dataSkipped["Meat Consumption Growth Rate"] + dataSkipped["Rice Consumption Growth Rate"] )/4, color = 'b',
        width = width, edgecolor = 'black',
        label='Consumption')

        self.ax.bar(r+width, (dataSkipped["Wheat Production Growth Rate"] + dataSkipped["Barley Production Growth Rate"] + dataSkipped["Meat Production Growth Rate"] + dataSkipped["Rice Production Growth Rate"] )/4, color = 'g',
                width = width, edgecolor = 'black',
                label='Production')

        self.ax.bar(r+width*2, dataSkipped["Hunger Annual Change"], color = 'y',
                width = width, edgecolor = 'black',
                label='Starvation')

        self.ax.set_xticks(r + width/2)
        self.ax.set_xticklabels(dataSkipped["Year"])
        self.ax.set(xlabel="Year", ylabel="Annual Rate", title="Comparison of consumption & production of common food items with starvation")
        self.ax.legend()


class analysisForImportsExportsAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(1000, 100), dpi=95)
        super().__init__(fig)
        self.setParent(parent)
        """ 
        Matplotlib Script
        """
        self.ax.bar(r, (dataSkipped["Wheat Imports Growth Rate"] + dataSkipped["Barley Imports Growth Rate"] + dataSkipped["Meat Imports Growth Rate"] + dataSkipped["Rice Imports Growth Rate"] )/4, color = 'b',
        width = width, edgecolor = 'black',
        label='Imports')

        self.ax.bar(r+width, (dataSkipped["Wheat Exports Growth Rate"] + dataSkipped["Barley Exports Growth Rate"] + dataSkipped["Meat Exports Growth Rate"] + dataSkipped["Rice Exports Growth Rate"] )/4, color = 'g',
                width = width, edgecolor = 'black',
                label='Exports')
        self.ax.bar(r+width*2, dataSkipped["Hunger Annual Change"], color = 'y',
                width = width, edgecolor = 'black',
                label='Starvation')
        self.ax.set_xticks(r + width/2)
        self.ax.set_xticklabels(dataSkipped["Year"])
        self.ax.set(xlabel="Year", ylabel="Annual Rate", title="Comparison of imports & exports of common food items with starvation")
        self.ax.legend()

class analysisForUnemploymentAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(1000, 100), dpi=95)
        super().__init__(fig)
        self.setParent(parent)
        """ 
        Matplotlib Script
        """
        self.ax.plot(dataSkipped["Year"], dataSkipped["Unemployment Per Year"], label="Unemployment")
        self.ax.plot(dataSkipped["Year"], dataSkipped["Hunger Annual Change"], label="Starvation")
        self.ax.set(xlabel="Unemployment", ylabel="Starvation", title="Trend of unemployment & starvation")
        self.ax.legend()

class analysisForInflationAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharey=True,sharex=True)
        super().__init__(fig)
        self.setParent(parent)
        """ 
        Matplotlib Script
        """
        self.ax1.plot(dataSkipped["Year"], dataSkipped["Inflation Annual Change"], label="Inflation")
        self.ax1.plot(dataSkipped["Year"], dataSkipped["Hunger Annual Change"], label="Starvation")
        self.ax1.set(xlabel="Inflation", ylabel="Starvation", title="Trend of inflation & starvation")
        self.ax1.legend()
        self.ax2.plot(dataSkipped["Year"], dataSkipped["Poverty Percent Under US $5.50 Per Day"], label="Under US $5.50 Per Day Earners")
        self.ax2.set(title="Trend Of Under US $5.50 Per Day Earners")

class analysisForPovertyAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(1000, 100), dpi=95)
        super().__init__(fig)
        self.setParent(parent)
        """ 
        Matplotlib Script
        """
        self.ax.plot(dataSkipped["Year"], dataSkipped["Poverty Annual Change"], label="Poverty")
        self.ax.plot(dataSkipped["Year"], dataSkipped["Hunger Annual Change"], label="Starvation")
        self.ax.set(xlabel="Poverty", ylabel="Starvation", title="Trend of inflation & starvation")
        self.ax.legend()

## End

# Main View also analysis view
class AnalysisWindow(QDialog):
    def __init__(self):
        super(AnalysisWindow, self).__init__()
        loadUi("Analysis.ui",self)
        self.switchToAnalysisView()
        self.predictionBtn.clicked.connect(self.switchToPredictionView)
        self.editBtn.clicked.connect(self.switchToEditView)

    def switchToAnalysisView(self):
        self.displayBtn.clicked.connect(self.displayAnalysisGraph)
        self.addOptionsForAnalysis()

    def switchToPredictionView(self):
        print("Currently in prediciton view")
        widget.setCurrentIndex(widget.currentIndex()+1)

    def switchToEditView(self):
        print("Currently in edit view")
        widget.setCurrentIndex(widget.currentIndex()+2)

    def addOptionsForAnalysis(self):
            self.comboBox.clear()
            self.comboBox.addItem("Analysis for consumption, production and starvation")
            self.comboBox.addItem("Analysis for imports, exports and starvation")
            self.comboBox.addItem("Analysis for starvation & unemployment")
            self.comboBox.addItem("Analysis for starvation & inflation")
            self.comboBox.addItem("Analysis for starvation & poverty")

    def displayAnalysisGraph(self):
        option = self.comboBox.currentText()
        clearContentArea(self.contentArea)
        if(option == "Analysis for consumption, production and starvation"):
                self.contentArea.addWidget(analysisForConsumptionProductionAndStarvation(self))
        elif(option == "Analysis for imports, exports and starvation"):
                self.contentArea.addWidget(analysisForImportsExportsAndStarvation(self))
        elif(option == "Analysis for starvation & unemployment"):
                self.contentArea.addWidget(analysisForUnemploymentAndStarvation(self))
        elif(option == "Analysis for starvation & inflation"):
                self.contentArea.addWidget(analysisForInflationAndStarvation(self))
        elif(option == "Analysis for starvation & poverty"):
                self.contentArea.addWidget(analysisForPovertyAndStarvation(self))

class MyTable(QTableWidget):
    fileName = ''
    def __init__(self, r, c, fileName):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()
        self.open(fileName)
        self.fileName = fileName

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self, fileName):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    def open(self, fileName):
        self.check_change = False
        path = os.getcwd() + '\\' + fileName
        if path != '':
            with open(path, newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True

    def save(self):
        path = os.getcwd() + '\\' + self.fileName
        if path != '':
            with open(path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

        
class EditWindow(QDialog):
    def __init__(self):
        super(EditWindow, self).__init__()
        loadUi("Analysis.ui",self)
        self.addOptionsForEdit()
        self.initializeSetup("Project-Dataset.csv")
        self.displayBtn.clicked.connect(self.displayTable)

    def displayTable(self):
        clearContentArea(self.contentArea)
        fileName = self.comboBox.currentText()
        self.initializeSetup(fileName)

    def addOptionsForEdit(self):
        self.comboBox.clear()
        self.comboBox.addItem("Project-Dataset.csv")
        self.comboBox.addItem("WFP Food Prices In Pakistan.csv")

    def initializeSetup(self, fileName):
        self.form_widget = MyTable(10, 10, fileName)
        self.contentArea.addWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)
        # Set up menu
        #save_action.triggered.connect(self.form_widget.save_sheet)
        self.shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut.activated.connect(self.form_widget.save)
        self.show()

    def quit_app(self):
        qApp.quit()


class PredictionWindow(QDialog):
    def __init__(self):
        super(PredictionWindow, self).__init__()
        loadUi("Analysis.ui",self)
# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(AnalysisWindow())
widget.addWidget(PredictionWindow())
widget.addWidget(EditWindow())
widget.setFixedWidth(935)
widget.setFixedHeight(566)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")