import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
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

class analysisForConsumptionProductionAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(1000, 100), dpi=95)
        super().__init__(fig)
        self.setParent(parent)
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
        self.ax.plot(dataSkipped["Year"], dataSkipped["Unemployment Per Year"], label="Unemployment")
        self.ax.plot(dataSkipped["Year"], dataSkipped["Hunger Annual Change"], label="Starvation")
        self.ax.set(xlabel="Unemployment", ylabel="Starvation", title="Trend of unemployment & starvation")
        self.ax.legend()

class analysisForInflationAndStarvation(FigureCanvas):
    def __init__(self, parent):
        fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharey=True,sharex=True)
        super().__init__(fig)
        self.setParent(parent)
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
        self.ax.plot(dataSkipped["Year"], dataSkipped["Poverty Annual Change"], label="Poverty")
        self.ax.plot(dataSkipped["Year"], dataSkipped["Hunger Annual Change"], label="Starvation")
        self.ax.set(xlabel="Poverty", ylabel="Starvation", title="Trend of inflation & starvation")
        self.ax.legend()

class AnalysisWindow(QDialog):
    def __init__(self):
        super(AnalysisWindow, self).__init__()
        loadUi("Analysis.ui",self)
        self.displayBtn.clicked.connect(self.displayAnalysisGraph)

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

class PredictionWindow(QDialog):
    def __init__(self):
        super(PredictionWindow, self).__init__()
        loadUi("Analysis.ui",self)
        # self.analysisBtn.clicked.connect(self.showAnalysisWindow)

class EditWindow(QDialog):
    def __init__(self):
        super(EditWindow, self).__init__()
        loadUi("Analysis.ui",self)
        # self.analysisBtn.clicked.connect(self.showAnalysisWindow)

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(AnalysisWindow())
widget.setFixedWidth(935)
widget.setFixedHeight(566)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")