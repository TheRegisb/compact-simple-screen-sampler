# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1181, 391)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.globalLayout = QHBoxLayout()
        self.globalLayout.setObjectName(u"globalLayout")
        self.selectorLayout = QVBoxLayout()
        self.selectorLayout.setObjectName(u"selectorLayout")
        self.sampleLayout = QHBoxLayout()
        self.sampleLayout.setObjectName(u"sampleLayout")
        self.sampleNavLayout = QVBoxLayout()
        self.sampleNavLayout.setObjectName(u"sampleNavLayout")
        self.sampleNavBtnPrev = QPushButton(self.centralwidget)
        self.sampleNavBtnPrev.setObjectName(u"sampleNavBtnPrev")
        self.sampleNavBtnPrev.setEnabled(False)
        icon = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.sampleNavBtnPrev.setIcon(icon)

        self.sampleNavLayout.addWidget(self.sampleNavBtnPrev)

        self.sampleNavBtnNext = QPushButton(self.centralwidget)
        self.sampleNavBtnNext.setObjectName(u"sampleNavBtnNext")
        self.sampleNavBtnNext.setEnabled(False)
        icon1 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.sampleNavBtnNext.setIcon(icon1)

        self.sampleNavLayout.addWidget(self.sampleNavBtnNext)


        self.sampleLayout.addLayout(self.sampleNavLayout)

        self.sampleDisplay = QGraphicsView(self.centralwidget)
        self.sampleDisplay.setObjectName(u"sampleDisplay")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleDisplay.sizePolicy().hasHeightForWidth())
        self.sampleDisplay.setSizePolicy(sizePolicy)
        self.sampleDisplay.setAcceptDrops(False)
        self.sampleDisplay.setFrameShape(QFrame.Box)
        self.sampleDisplay.setFrameShadow(QFrame.Sunken)
        self.sampleDisplay.setInteractive(False)

        self.sampleLayout.addWidget(self.sampleDisplay)


        self.selectorLayout.addLayout(self.sampleLayout)

        self.sampleBtn = QPushButton(self.centralwidget)
        self.sampleBtn.setObjectName(u"sampleBtn")
        icon2 = QIcon()
        iconThemeName = u"camera-photo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.sampleBtn.setIcon(icon2)

        self.selectorLayout.addWidget(self.sampleBtn)

        self.sampleConfigSeparator = QFrame(self.centralwidget)
        self.sampleConfigSeparator.setObjectName(u"sampleConfigSeparator")
        self.sampleConfigSeparator.setFrameShape(QFrame.HLine)
        self.sampleConfigSeparator.setFrameShadow(QFrame.Sunken)

        self.selectorLayout.addWidget(self.sampleConfigSeparator)

        self.selectionConfigLabel = QLabel(self.centralwidget)
        self.selectionConfigLabel.setObjectName(u"selectionConfigLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectionConfigLabel.sizePolicy().hasHeightForWidth())
        self.selectionConfigLabel.setSizePolicy(sizePolicy1)
        self.selectionConfigLabel.setAlignment(Qt.AlignCenter)

        self.selectorLayout.addWidget(self.selectionConfigLabel)

        self.selectionConfigLayout = QGridLayout()
        self.selectionConfigLayout.setObjectName(u"selectionConfigLayout")
        self.selectionConfigRadSingle = QRadioButton(self.centralwidget)
        self.selectionConfigRadSingle.setObjectName(u"selectionConfigRadSingle")
        self.selectionConfigRadSingle.setChecked(True)

        self.selectionConfigLayout.addWidget(self.selectionConfigRadSingle, 2, 0, 1, 1)


        self.selectorLayout.addLayout(self.selectionConfigLayout)

        self.selectionConfigRadRegion = QRadioButton(self.centralwidget)
        self.selectionConfigRadRegion.setObjectName(u"selectionConfigRadRegion")

        self.selectorLayout.addWidget(self.selectionConfigRadRegion)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.selectorLayout.addItem(self.verticalSpacer_3)


        self.globalLayout.addLayout(self.selectorLayout)

        self.selectorDataSeparator = QFrame(self.centralwidget)
        self.selectorDataSeparator.setObjectName(u"selectorDataSeparator")
        self.selectorDataSeparator.setFrameShape(QFrame.VLine)
        self.selectorDataSeparator.setFrameShadow(QFrame.Sunken)

        self.globalLayout.addWidget(self.selectorDataSeparator)

        self.dataAndFmtLayout = QVBoxLayout()
        self.dataAndFmtLayout.setObjectName(u"dataAndFmtLayout")
        self.dataRgbLayout = QGridLayout()
        self.dataRgbLayout.setObjectName(u"dataRgbLayout")
        self.floatTextB = QLineEdit(self.centralwidget)
        self.floatTextB.setObjectName(u"floatTextB")
        self.floatTextB.setEnabled(True)
        self.floatTextB.setAlignment(Qt.AlignCenter)
        self.floatTextB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.floatTextB, 2, 4, 1, 1)

        self.floatBtnCopyRGB = QPushButton(self.centralwidget)
        self.floatBtnCopyRGB.setObjectName(u"floatBtnCopyRGB")
        icon3 = QIcon()
        iconThemeName = u"edit-copy"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.floatBtnCopyRGB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.floatBtnCopyRGB, 4, 5, 1, 1)

        self.hexBtnCopyR = QPushButton(self.centralwidget)
        self.hexBtnCopyR.setObjectName(u"hexBtnCopyR")
        self.hexBtnCopyR.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.hexBtnCopyR, 0, 8, 1, 1)

        self.hexBtnCopyG = QPushButton(self.centralwidget)
        self.hexBtnCopyG.setObjectName(u"hexBtnCopyG")
        self.hexBtnCopyG.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.hexBtnCopyG, 1, 8, 1, 1)

        self.intBtnCopyR = QPushButton(self.centralwidget)
        self.intBtnCopyR.setObjectName(u"intBtnCopyR")
        self.intBtnCopyR.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.intBtnCopyR.sizePolicy().hasHeightForWidth())
        self.intBtnCopyR.setSizePolicy(sizePolicy2)
        self.intBtnCopyR.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.intBtnCopyR, 0, 2, 1, 1)

        self.intBtnCopyG = QPushButton(self.centralwidget)
        self.intBtnCopyG.setObjectName(u"intBtnCopyG")
        self.intBtnCopyG.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.intBtnCopyG, 1, 2, 1, 1)

        self.intTextG = QLineEdit(self.centralwidget)
        self.intTextG.setObjectName(u"intTextG")
        self.intTextG.setEnabled(True)
        self.intTextG.setAlignment(Qt.AlignCenter)
        self.intTextG.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.intTextG, 1, 1, 1, 1)

        self.intBtnCopyRGB = QPushButton(self.centralwidget)
        self.intBtnCopyRGB.setObjectName(u"intBtnCopyRGB")
        self.intBtnCopyRGB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.intBtnCopyRGB, 4, 2, 1, 1)

        self.intTextRGB = QLineEdit(self.centralwidget)
        self.intTextRGB.setObjectName(u"intTextRGB")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.intTextRGB.sizePolicy().hasHeightForWidth())
        self.intTextRGB.setSizePolicy(sizePolicy3)
        self.intTextRGB.setAlignment(Qt.AlignCenter)
        self.intTextRGB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.intTextRGB, 4, 1, 1, 1)

        self.labelRGB = QLabel(self.centralwidget)
        self.labelRGB.setObjectName(u"labelRGB")
        self.labelRGB.setAlignment(Qt.AlignCenter)

        self.dataRgbLayout.addWidget(self.labelRGB, 4, 0, 1, 1)

        self.floatTextR = QLineEdit(self.centralwidget)
        self.floatTextR.setObjectName(u"floatTextR")
        self.floatTextR.setEnabled(True)
        self.floatTextR.setAlignment(Qt.AlignCenter)
        self.floatTextR.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.floatTextR, 0, 4, 1, 1)

        self.hexBtnCopyB = QPushButton(self.centralwidget)
        self.hexBtnCopyB.setObjectName(u"hexBtnCopyB")
        self.hexBtnCopyB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.hexBtnCopyB, 2, 8, 1, 1)

        self.floatTextG = QLineEdit(self.centralwidget)
        self.floatTextG.setObjectName(u"floatTextG")
        self.floatTextG.setEnabled(True)
        self.floatTextG.setAlignment(Qt.AlignCenter)
        self.floatTextG.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.floatTextG, 1, 4, 1, 1)

        self.hexTextR = QLineEdit(self.centralwidget)
        self.hexTextR.setObjectName(u"hexTextR")
        self.hexTextR.setEnabled(True)
        self.hexTextR.setAlignment(Qt.AlignCenter)
        self.hexTextR.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.hexTextR, 0, 7, 1, 1)

        self.labelG = QLabel(self.centralwidget)
        self.labelG.setObjectName(u"labelG")
        self.labelG.setAlignment(Qt.AlignCenter)

        self.dataRgbLayout.addWidget(self.labelG, 1, 0, 1, 1)

        self.floatHexSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.dataRgbLayout.addItem(self.floatHexSpacer, 0, 6, 1, 1)

        self.hexTextG = QLineEdit(self.centralwidget)
        self.hexTextG.setObjectName(u"hexTextG")
        self.hexTextG.setEnabled(True)
        self.hexTextG.setAlignment(Qt.AlignCenter)
        self.hexTextG.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.hexTextG, 1, 7, 1, 1)

        self.hexBtnCopyRGB = QPushButton(self.centralwidget)
        self.hexBtnCopyRGB.setObjectName(u"hexBtnCopyRGB")
        self.hexBtnCopyRGB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.hexBtnCopyRGB, 4, 8, 1, 1)

        self.intFloatSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.dataRgbLayout.addItem(self.intFloatSpacer, 0, 3, 1, 1)

        self.hexTextRGB = QLineEdit(self.centralwidget)
        self.hexTextRGB.setObjectName(u"hexTextRGB")
        self.hexTextRGB.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.hexTextRGB.sizePolicy().hasHeightForWidth())
        self.hexTextRGB.setSizePolicy(sizePolicy3)
        self.hexTextRGB.setAlignment(Qt.AlignCenter)
        self.hexTextRGB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.hexTextRGB, 4, 7, 1, 1)

        self.labelR = QLabel(self.centralwidget)
        self.labelR.setObjectName(u"labelR")
        self.labelR.setAlignment(Qt.AlignCenter)

        self.dataRgbLayout.addWidget(self.labelR, 0, 0, 1, 1)

        self.labelB = QLabel(self.centralwidget)
        self.labelB.setObjectName(u"labelB")
        self.labelB.setAlignment(Qt.AlignCenter)

        self.dataRgbLayout.addWidget(self.labelB, 2, 0, 1, 1)

        self.intTextB = QLineEdit(self.centralwidget)
        self.intTextB.setObjectName(u"intTextB")
        self.intTextB.setEnabled(True)
        self.intTextB.setAlignment(Qt.AlignCenter)
        self.intTextB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.intTextB, 2, 1, 1, 1)

        self.floatBtnCopyG = QPushButton(self.centralwidget)
        self.floatBtnCopyG.setObjectName(u"floatBtnCopyG")
        self.floatBtnCopyG.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.floatBtnCopyG, 1, 5, 1, 1)

        self.floatBtnCopyB = QPushButton(self.centralwidget)
        self.floatBtnCopyB.setObjectName(u"floatBtnCopyB")
        self.floatBtnCopyB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.floatBtnCopyB, 2, 5, 1, 1)

        self.intBtnCopyB = QPushButton(self.centralwidget)
        self.intBtnCopyB.setObjectName(u"intBtnCopyB")
        self.intBtnCopyB.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.intBtnCopyB, 2, 2, 1, 1)

        self.soloCombinedSpacer = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.dataRgbLayout.addItem(self.soloCombinedSpacer, 3, 1, 1, 1)

        self.floatBtnCopyR = QPushButton(self.centralwidget)
        self.floatBtnCopyR.setObjectName(u"floatBtnCopyR")
        self.floatBtnCopyR.setIcon(icon3)

        self.dataRgbLayout.addWidget(self.floatBtnCopyR, 0, 5, 1, 1)

        self.hexTextB = QLineEdit(self.centralwidget)
        self.hexTextB.setObjectName(u"hexTextB")
        self.hexTextB.setEnabled(True)
        self.hexTextB.setAlignment(Qt.AlignCenter)
        self.hexTextB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.hexTextB, 2, 7, 1, 1)

        self.floatTextRGB = QLineEdit(self.centralwidget)
        self.floatTextRGB.setObjectName(u"floatTextRGB")
        self.floatTextRGB.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.floatTextRGB.sizePolicy().hasHeightForWidth())
        self.floatTextRGB.setSizePolicy(sizePolicy3)
        self.floatTextRGB.setAlignment(Qt.AlignCenter)
        self.floatTextRGB.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.floatTextRGB, 4, 4, 1, 1)

        self.intTextR = QLineEdit(self.centralwidget)
        self.intTextR.setObjectName(u"intTextR")
        self.intTextR.setEnabled(True)
        self.intTextR.setAlignment(Qt.AlignCenter)
        self.intTextR.setReadOnly(True)

        self.dataRgbLayout.addWidget(self.intTextR, 0, 1, 1, 1)


        self.dataAndFmtLayout.addLayout(self.dataRgbLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.dataAndFmtLayout.addWidget(self.line)

        self.dataHslLayout = QGridLayout()
        self.dataHslLayout.setObjectName(u"dataHslLayout")
        self.labelHSL = QLabel(self.centralwidget)
        self.labelHSL.setObjectName(u"labelHSL")
        self.labelHSL.setAlignment(Qt.AlignCenter)

        self.dataHslLayout.addWidget(self.labelHSL, 4, 0, 1, 1)

        self.floatBtnCopyH = QPushButton(self.centralwidget)
        self.floatBtnCopyH.setObjectName(u"floatBtnCopyH")
        self.floatBtnCopyH.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.floatBtnCopyH.sizePolicy().hasHeightForWidth())
        self.floatBtnCopyH.setSizePolicy(sizePolicy2)
        self.floatBtnCopyH.setIcon(icon3)

        self.dataHslLayout.addWidget(self.floatBtnCopyH, 0, 5, 1, 1)

        self.intBtnCopyS = QPushButton(self.centralwidget)
        self.intBtnCopyS.setObjectName(u"intBtnCopyS")
        self.intBtnCopyS.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.intBtnCopyS.sizePolicy().hasHeightForWidth())
        self.intBtnCopyS.setSizePolicy(sizePolicy2)
        self.intBtnCopyS.setIcon(icon3)

        self.dataHslLayout.addWidget(self.intBtnCopyS, 1, 2, 1, 1)

        self.intFloatSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.dataHslLayout.addItem(self.intFloatSpacer_2, 0, 3, 1, 1)

        self.soloCombinedSpacer_2 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.dataHslLayout.addItem(self.soloCombinedSpacer_2, 3, 1, 1, 1)

        self.intTextHSL = QLineEdit(self.centralwidget)
        self.intTextHSL.setObjectName(u"intTextHSL")
        self.intTextHSL.setEnabled(True)
        self.intTextHSL.setAlignment(Qt.AlignCenter)
        self.intTextHSL.setReadOnly(True)

        self.dataHslLayout.addWidget(self.intTextHSL, 4, 1, 1, 1)

        self.floatBtnCopyL = QPushButton(self.centralwidget)
        self.floatBtnCopyL.setObjectName(u"floatBtnCopyL")
        self.floatBtnCopyL.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.floatBtnCopyL.sizePolicy().hasHeightForWidth())
        self.floatBtnCopyL.setSizePolicy(sizePolicy2)
        self.floatBtnCopyL.setIcon(icon3)

        self.dataHslLayout.addWidget(self.floatBtnCopyL, 2, 5, 1, 1)

        self.floatTextS = QLineEdit(self.centralwidget)
        self.floatTextS.setObjectName(u"floatTextS")
        self.floatTextS.setEnabled(True)
        self.floatTextS.setAlignment(Qt.AlignCenter)
        self.floatTextS.setReadOnly(True)

        self.dataHslLayout.addWidget(self.floatTextS, 1, 4, 1, 1)

        self.intTextS = QLineEdit(self.centralwidget)
        self.intTextS.setObjectName(u"intTextS")
        self.intTextS.setEnabled(True)
        self.intTextS.setAlignment(Qt.AlignCenter)
        self.intTextS.setReadOnly(True)

        self.dataHslLayout.addWidget(self.intTextS, 1, 1, 1, 1)

        self.intBtnCopyHSL = QPushButton(self.centralwidget)
        self.intBtnCopyHSL.setObjectName(u"intBtnCopyHSL")
        self.intBtnCopyHSL.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.intBtnCopyHSL.sizePolicy().hasHeightForWidth())
        self.intBtnCopyHSL.setSizePolicy(sizePolicy2)
        self.intBtnCopyHSL.setIcon(icon3)

        self.dataHslLayout.addWidget(self.intBtnCopyHSL, 4, 2, 1, 1)

        self.intBtnCopyL = QPushButton(self.centralwidget)
        self.intBtnCopyL.setObjectName(u"intBtnCopyL")
        self.intBtnCopyL.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.intBtnCopyL.sizePolicy().hasHeightForWidth())
        self.intBtnCopyL.setSizePolicy(sizePolicy2)
        self.intBtnCopyL.setIcon(icon3)

        self.dataHslLayout.addWidget(self.intBtnCopyL, 2, 2, 1, 1)

        self.labelS = QLabel(self.centralwidget)
        self.labelS.setObjectName(u"labelS")
        self.labelS.setAlignment(Qt.AlignCenter)

        self.dataHslLayout.addWidget(self.labelS, 1, 0, 1, 1)

        self.floatTextHSL = QLineEdit(self.centralwidget)
        self.floatTextHSL.setObjectName(u"floatTextHSL")
        self.floatTextHSL.setEnabled(True)
        self.floatTextHSL.setAlignment(Qt.AlignCenter)
        self.floatTextHSL.setReadOnly(True)

        self.dataHslLayout.addWidget(self.floatTextHSL, 4, 4, 1, 1)

        self.floatBtnCopyS = QPushButton(self.centralwidget)
        self.floatBtnCopyS.setObjectName(u"floatBtnCopyS")
        self.floatBtnCopyS.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.floatBtnCopyS.sizePolicy().hasHeightForWidth())
        self.floatBtnCopyS.setSizePolicy(sizePolicy2)
        self.floatBtnCopyS.setIcon(icon3)

        self.dataHslLayout.addWidget(self.floatBtnCopyS, 1, 5, 1, 1)

        self.intTextL = QLineEdit(self.centralwidget)
        self.intTextL.setObjectName(u"intTextL")
        self.intTextL.setEnabled(True)
        self.intTextL.setAlignment(Qt.AlignCenter)
        self.intTextL.setReadOnly(True)

        self.dataHslLayout.addWidget(self.intTextL, 2, 1, 1, 1)

        self.floatTextH = QLineEdit(self.centralwidget)
        self.floatTextH.setObjectName(u"floatTextH")
        self.floatTextH.setEnabled(True)
        self.floatTextH.setAlignment(Qt.AlignCenter)
        self.floatTextH.setReadOnly(True)

        self.dataHslLayout.addWidget(self.floatTextH, 0, 4, 1, 1)

        self.labelL = QLabel(self.centralwidget)
        self.labelL.setObjectName(u"labelL")
        self.labelL.setAlignment(Qt.AlignCenter)

        self.dataHslLayout.addWidget(self.labelL, 2, 0, 1, 1)

        self.intBtnCopyH = QPushButton(self.centralwidget)
        self.intBtnCopyH.setObjectName(u"intBtnCopyH")
        self.intBtnCopyH.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.intBtnCopyH.sizePolicy().hasHeightForWidth())
        self.intBtnCopyH.setSizePolicy(sizePolicy2)
        self.intBtnCopyH.setIcon(icon3)

        self.dataHslLayout.addWidget(self.intBtnCopyH, 0, 2, 1, 1)

        self.floatBtnCopyHSL = QPushButton(self.centralwidget)
        self.floatBtnCopyHSL.setObjectName(u"floatBtnCopyHSL")
        self.floatBtnCopyHSL.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.floatBtnCopyHSL.sizePolicy().hasHeightForWidth())
        self.floatBtnCopyHSL.setSizePolicy(sizePolicy2)
        self.floatBtnCopyHSL.setIcon(icon3)

        self.dataHslLayout.addWidget(self.floatBtnCopyHSL, 4, 5, 1, 1)

        self.labelH = QLabel(self.centralwidget)
        self.labelH.setObjectName(u"labelH")
        self.labelH.setAlignment(Qt.AlignCenter)

        self.dataHslLayout.addWidget(self.labelH, 0, 0, 1, 1)

        self.floatTextL = QLineEdit(self.centralwidget)
        self.floatTextL.setObjectName(u"floatTextL")
        self.floatTextL.setEnabled(True)
        self.floatTextL.setAlignment(Qt.AlignCenter)
        self.floatTextL.setReadOnly(True)

        self.dataHslLayout.addWidget(self.floatTextL, 2, 4, 1, 1)

        self.intTextH = QLineEdit(self.centralwidget)
        self.intTextH.setObjectName(u"intTextH")
        self.intTextH.setEnabled(True)
        self.intTextH.setAlignment(Qt.AlignCenter)
        self.intTextH.setReadOnly(True)

        self.dataHslLayout.addWidget(self.intTextH, 0, 1, 1, 1)


        self.dataAndFmtLayout.addLayout(self.dataHslLayout)

        self.dataFmtSeparator = QFrame(self.centralwidget)
        self.dataFmtSeparator.setObjectName(u"dataFmtSeparator")
        self.dataFmtSeparator.setFrameShape(QFrame.HLine)
        self.dataFmtSeparator.setFrameShadow(QFrame.Sunken)

        self.dataAndFmtLayout.addWidget(self.dataFmtSeparator)

        self.fmtLayout = QHBoxLayout()
        self.fmtLayout.setObjectName(u"fmtLayout")
        self.fmtArrLabel = QLabel(self.centralwidget)
        self.fmtArrLabel.setObjectName(u"fmtArrLabel")

        self.fmtLayout.addWidget(self.fmtArrLabel)

        self.fmtArrTextStart = QLineEdit(self.centralwidget)
        self.fmtArrTextStart.setObjectName(u"fmtArrTextStart")
        self.fmtArrTextStart.setAlignment(Qt.AlignCenter)

        self.fmtLayout.addWidget(self.fmtArrTextStart)

        self.fmtArrTextSep = QLineEdit(self.centralwidget)
        self.fmtArrTextSep.setObjectName(u"fmtArrTextSep")
        self.fmtArrTextSep.setAlignment(Qt.AlignCenter)

        self.fmtLayout.addWidget(self.fmtArrTextSep)

        self.fmtArrTextEnd = QLineEdit(self.centralwidget)
        self.fmtArrTextEnd.setObjectName(u"fmtArrTextEnd")
        self.fmtArrTextEnd.setAlignment(Qt.AlignCenter)

        self.fmtLayout.addWidget(self.fmtArrTextEnd)

        self.fmtArrChkSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.fmtLayout.addItem(self.fmtArrChkSpacer)

        self.fmtLabelDecPrec = QLabel(self.centralwidget)
        self.fmtLabelDecPrec.setObjectName(u"fmtLabelDecPrec")

        self.fmtLayout.addWidget(self.fmtLabelDecPrec)

        self.fmtSpinDecPrec = QSpinBox(self.centralwidget)
        self.fmtSpinDecPrec.setObjectName(u"fmtSpinDecPrec")
        self.fmtSpinDecPrec.setMinimum(1)
        self.fmtSpinDecPrec.setMaximum(32)
        self.fmtSpinDecPrec.setValue(5)

        self.fmtLayout.addWidget(self.fmtSpinDecPrec)

        self.fmtDecPrecSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.fmtLayout.addItem(self.fmtDecPrecSpacer)

        self.fmtChkDecimalsSep = QCheckBox(self.centralwidget)
        self.fmtChkDecimalsSep.setObjectName(u"fmtChkDecimalsSep")

        self.fmtLayout.addWidget(self.fmtChkDecimalsSep)

        self.fmtChkHexNoHash = QCheckBox(self.centralwidget)
        self.fmtChkHexNoHash.setObjectName(u"fmtChkHexNoHash")

        self.fmtLayout.addWidget(self.fmtChkHexNoHash)

        self.fmtChkSLPercentage = QCheckBox(self.centralwidget)
        self.fmtChkSLPercentage.setObjectName(u"fmtChkSLPercentage")
        self.fmtChkSLPercentage.setChecked(True)

        self.fmtLayout.addWidget(self.fmtChkSLPercentage)


        self.dataAndFmtLayout.addLayout(self.fmtLayout)


        self.globalLayout.addLayout(self.dataAndFmtLayout)


        self.gridLayout.addLayout(self.globalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.sampleBtn, self.selectionConfigRadSingle)
        QWidget.setTabOrder(self.selectionConfigRadSingle, self.selectionConfigRadRegion)
        QWidget.setTabOrder(self.selectionConfigRadRegion, self.intTextR)
        QWidget.setTabOrder(self.intTextR, self.intBtnCopyR)
        QWidget.setTabOrder(self.intBtnCopyR, self.intTextG)
        QWidget.setTabOrder(self.intTextG, self.intBtnCopyG)
        QWidget.setTabOrder(self.intBtnCopyG, self.intTextB)
        QWidget.setTabOrder(self.intTextB, self.intBtnCopyB)
        QWidget.setTabOrder(self.intBtnCopyB, self.intTextRGB)
        QWidget.setTabOrder(self.intTextRGB, self.intBtnCopyRGB)
        QWidget.setTabOrder(self.intBtnCopyRGB, self.floatTextR)
        QWidget.setTabOrder(self.floatTextR, self.floatBtnCopyR)
        QWidget.setTabOrder(self.floatBtnCopyR, self.floatTextG)
        QWidget.setTabOrder(self.floatTextG, self.floatBtnCopyG)
        QWidget.setTabOrder(self.floatBtnCopyG, self.floatTextB)
        QWidget.setTabOrder(self.floatTextB, self.floatBtnCopyB)
        QWidget.setTabOrder(self.floatBtnCopyB, self.floatTextRGB)
        QWidget.setTabOrder(self.floatTextRGB, self.floatBtnCopyRGB)
        QWidget.setTabOrder(self.floatBtnCopyRGB, self.hexTextR)
        QWidget.setTabOrder(self.hexTextR, self.hexBtnCopyR)
        QWidget.setTabOrder(self.hexBtnCopyR, self.hexTextG)
        QWidget.setTabOrder(self.hexTextG, self.hexBtnCopyG)
        QWidget.setTabOrder(self.hexBtnCopyG, self.hexTextB)
        QWidget.setTabOrder(self.hexTextB, self.hexBtnCopyB)
        QWidget.setTabOrder(self.hexBtnCopyB, self.hexTextRGB)
        QWidget.setTabOrder(self.hexTextRGB, self.hexBtnCopyRGB)
        QWidget.setTabOrder(self.hexBtnCopyRGB, self.intTextH)
        QWidget.setTabOrder(self.intTextH, self.intBtnCopyH)
        QWidget.setTabOrder(self.intBtnCopyH, self.intTextS)
        QWidget.setTabOrder(self.intTextS, self.intBtnCopyS)
        QWidget.setTabOrder(self.intBtnCopyS, self.intTextL)
        QWidget.setTabOrder(self.intTextL, self.intBtnCopyL)
        QWidget.setTabOrder(self.intBtnCopyL, self.intTextHSL)
        QWidget.setTabOrder(self.intTextHSL, self.intBtnCopyHSL)
        QWidget.setTabOrder(self.intBtnCopyHSL, self.floatTextH)
        QWidget.setTabOrder(self.floatTextH, self.floatBtnCopyH)
        QWidget.setTabOrder(self.floatBtnCopyH, self.floatTextS)
        QWidget.setTabOrder(self.floatTextS, self.floatBtnCopyS)
        QWidget.setTabOrder(self.floatBtnCopyS, self.floatTextL)
        QWidget.setTabOrder(self.floatTextL, self.floatBtnCopyL)
        QWidget.setTabOrder(self.floatBtnCopyL, self.floatTextHSL)
        QWidget.setTabOrder(self.floatTextHSL, self.floatBtnCopyHSL)
        QWidget.setTabOrder(self.floatBtnCopyHSL, self.fmtArrTextStart)
        QWidget.setTabOrder(self.fmtArrTextStart, self.fmtArrTextSep)
        QWidget.setTabOrder(self.fmtArrTextSep, self.fmtArrTextEnd)
        QWidget.setTabOrder(self.fmtArrTextEnd, self.fmtSpinDecPrec)
        QWidget.setTabOrder(self.fmtSpinDecPrec, self.fmtChkDecimalsSep)
        QWidget.setTabOrder(self.fmtChkDecimalsSep, self.fmtChkHexNoHash)
        QWidget.setTabOrder(self.fmtChkHexNoHash, self.fmtChkSLPercentage)
        QWidget.setTabOrder(self.fmtChkSLPercentage, self.sampleNavBtnPrev)
        QWidget.setTabOrder(self.sampleNavBtnPrev, self.sampleNavBtnNext)
        QWidget.setTabOrder(self.sampleNavBtnNext, self.sampleDisplay)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Compact Simple Screen Sampler", None))
        self.sampleNavBtnPrev.setText("")
        self.sampleNavBtnNext.setText("")
        self.sampleBtn.setText(QCoreApplication.translate("MainWindow", u" Sample screen", None))
        self.selectionConfigLabel.setText(QCoreApplication.translate("MainWindow", u"Selection Mode", None))
        self.selectionConfigRadSingle.setText(QCoreApplication.translate("MainWindow", u"Single pixel", None))
        self.selectionConfigRadRegion.setText(QCoreApplication.translate("MainWindow", u"Region average", None))
        self.floatTextB.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.floatBtnCopyRGB.setText("")
        self.hexBtnCopyR.setText("")
        self.hexBtnCopyG.setText("")
        self.intBtnCopyR.setText("")
        self.intBtnCopyG.setText("")
        self.intTextG.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.intBtnCopyRGB.setText("")
        self.intTextRGB.setText(QCoreApplication.translate("MainWindow", u"(0, 0, 0)", None))
        self.labelRGB.setText(QCoreApplication.translate("MainWindow", u"RGB", None))
        self.floatTextR.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.hexBtnCopyB.setText("")
        self.floatTextG.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.hexTextR.setText(QCoreApplication.translate("MainWindow", u"#00", None))
        self.labelG.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.hexTextG.setText(QCoreApplication.translate("MainWindow", u"#00", None))
        self.hexBtnCopyRGB.setText("")
        self.hexTextRGB.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.labelR.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.labelB.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.intTextB.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.floatBtnCopyG.setText("")
        self.floatBtnCopyB.setText("")
        self.intBtnCopyB.setText("")
        self.floatBtnCopyR.setText("")
        self.hexTextB.setText(QCoreApplication.translate("MainWindow", u"#00", None))
        self.floatTextRGB.setText(QCoreApplication.translate("MainWindow", u"(0.0, 0.0, 0.0)", None))
        self.intTextR.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelHSL.setText(QCoreApplication.translate("MainWindow", u"HSL", None))
        self.floatBtnCopyH.setText("")
        self.intBtnCopyS.setText("")
        self.intTextHSL.setText(QCoreApplication.translate("MainWindow", u"(0, 0.0%, 0.0%)", None))
        self.floatBtnCopyL.setText("")
        self.floatTextS.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.intTextS.setText(QCoreApplication.translate("MainWindow", u"0.0%", None))
        self.intBtnCopyHSL.setText("")
        self.intBtnCopyL.setText("")
        self.labelS.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.floatTextHSL.setText(QCoreApplication.translate("MainWindow", u"(0.0, 0.0, 0.0)", None))
        self.floatBtnCopyS.setText("")
        self.intTextL.setText(QCoreApplication.translate("MainWindow", u"0.0%", None))
        self.floatTextH.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelL.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.intBtnCopyH.setText("")
        self.floatBtnCopyHSL.setText("")
        self.labelH.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.floatTextL.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.intTextH.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fmtArrLabel.setText(QCoreApplication.translate("MainWindow", u"Array format", None))
        self.fmtArrTextStart.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.fmtArrTextStart.setPlaceholderText("")
        self.fmtArrTextSep.setText(QCoreApplication.translate("MainWindow", u", ", None))
        self.fmtArrTextSep.setPlaceholderText("")
        self.fmtArrTextEnd.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.fmtArrTextEnd.setPlaceholderText("")
        self.fmtLabelDecPrec.setText(QCoreApplication.translate("MainWindow", u"Decimal precision", None))
        self.fmtChkDecimalsSep.setText(QCoreApplication.translate("MainWindow", u"Use comma for decimals", None))
        self.fmtChkHexNoHash.setText(QCoreApplication.translate("MainWindow", u"No hash symbol", None))
        self.fmtChkSLPercentage.setText(QCoreApplication.translate("MainWindow", u"SL as percentage", None))
    # retranslateUi

