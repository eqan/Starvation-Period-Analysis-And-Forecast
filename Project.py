import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class AnalysisWindow(QDialog):
    def __init__(self):
        super(AnalysisWindow, self).__init__()
        loadUi("Analysis.ui",self)
        # self.analysisBtn.clicked.connect(self.showAnalysisWindow)

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
widget.setFixedHeight(441)
widget.setFixedWidth(621)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")