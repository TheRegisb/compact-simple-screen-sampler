#!/usr/bin/python3

# Copyright (c) 2023 Régis Berthelot

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

from sys import argv
from typing import Dict, Iterable, Optional, Union
from numbers import Number
from decimal import Decimal

from PySide6.QtGui import (QGuiApplication, QColorConstants, QCursor, QScreen, QColor, QPixmap, QBrush, QClipboard)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsScene, QLineEdit)
from PySide6.QtCore import (Qt, Signal, QRect)

from ui.main_window import Ui_MainWindow
from utils.Maths import clamp
from utils.Arrays import (ArrayFormatter, ActiveArray)
from widgets.ColorPickers import (PixelColorPicker, RegionColorPicker)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # UI setup
        self.setupUi(self)
        self.setWindowTitle("cs3")
        # Class members
        self.arrayFormatter = ArrayFormatter(
            self.fmtArrTextStart.text(),
            self.fmtArrTextSep.text(),
            self.fmtArrTextEnd.text()
        )
        self.SAMPLE_DIM = 200
        self.sampleScene = QGraphicsScene(0, 0, self.SAMPLE_DIM, self.SAMPLE_DIM)
        self.sampleItem = QGraphicsRectItem(0, 0, self.SAMPLE_DIM, self.SAMPLE_DIM)
        self.colors = ActiveArray()
        # Slots setup
        self.sampleBtn.clicked.connect(self.sampleScreenSlot)
        self.sampleNavBtnPrev.clicked.connect(self.navPreviousSampleSlot)
        self.sampleNavBtnNext.clicked.connect(self.navNextSampleSlot)
        self.fmtSpinDecPrec.valueChanged[int].connect(self.changeFormatSlot)
        self.fmtChkDecimalsSep.stateChanged[int].connect(self.changeFormatSlot)
        self.fmtChkHexNoHash.stateChanged[int].connect(self.changeFormatSlot)
        self.fmtChkSLPercentage.stateChanged[int].connect(self.changeFormatSlot)
        self.fmtArrTextStart.textChanged[str].connect(self.arrayFormatterStartSlot)
        self.fmtArrTextSep.textChanged[str].connect(self.arrayFormatterSepSlot)
        self.fmtArrTextEnd.textChanged[str].connect(self.arrayFormatterEndSlot)
        self.intBtnCopyR.clicked.connect(lambda x: self.fieldToClipboard(self.intTextR))
        self.intBtnCopyG.clicked.connect(lambda x: self.fieldToClipboard(self.intTextG))
        self.intBtnCopyB.clicked.connect(lambda x: self.fieldToClipboard(self.intTextB))
        self.intBtnCopyRGB.clicked.connect(lambda x: self.fieldToClipboard(self.intTextRGB))
        self.floatBtnCopyR.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextR))
        self.floatBtnCopyG.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextG))
        self.floatBtnCopyB.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextB))
        self.floatBtnCopyRGB.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextRGB))
        self.hexBtnCopyR.clicked.connect(lambda x: self.fieldToClipboard(self.hexTextR))
        self.hexBtnCopyG.clicked.connect(lambda x: self.fieldToClipboard(self.hexTextG))
        self.hexBtnCopyB.clicked.connect(lambda x: self.fieldToClipboard(self.hexTextB))
        self.hexBtnCopyRGB.clicked.connect(lambda x: self.fieldToClipboard(self.hexTextRGB))
        self.intBtnCopyH.clicked.connect(lambda x: self.fieldToClipboard(self.intTextH))
        self.intBtnCopyS.clicked.connect(lambda x: self.fieldToClipboard(self.intTextS))
        self.intBtnCopyL.clicked.connect(lambda x: self.fieldToClipboard(self.intTextL))
        self.intBtnCopyHSL.clicked.connect(lambda x: self.fieldToClipboard(self.intTextHSL))
        self.floatBtnCopyH.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextH))
        self.floatBtnCopyS.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextS))
        self.floatBtnCopyL.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextL))
        self.floatBtnCopyHSL.clicked.connect(lambda x: self.fieldToClipboard(self.floatTextHSL))
        # Visual init
        self.sampleItem.setBrush(QBrush(QColorConstants.Black))
        self.sampleScene.addItem(self.sampleItem)
        self.sampleDisplay.setScene(self.sampleScene)
        self.sampleDisplay.show()


    def fieldToClipboard(self, field: QLineEdit):
        QGuiApplication.clipboard().setText(field.text())


    def changeFormatSlot(self):
        self.fillColorData()


    def sampleScreenSlot(self):
        if self.selectionConfigRadSingle.isChecked():
            cp = PixelColorPicker(self)
        else:
            cp = RegionColorPicker(self)
        cp.colorSample.connect(self.addNewColor)


    def navPreviousSampleSlot(self):
        self.colors.moveToPrevious()
        self.refreshColorUi()


    def navNextSampleSlot(self):
        self.colors.moveToNext()
        self.refreshColorUi()


    def addNewColor(self, color: Optional[QColor]):
        if color is None:
            return
        self.colors.append(color)
        self.refreshColorUi()


    def refreshColorUi(self):
        self.updateSampleNavigation()
        self.fillColorData()
        self.sampleItem.setBrush(self.colors.getActive())


    def updateSampleNavigation(self):
        self.sampleNavBtnPrev.setEnabled(not self.colors.atStart())
        self.sampleNavBtnNext.setEnabled(not self.colors.atEnd())


    def arrayFormatterStartSlot(self):
        self.arrayFormatter.setStart(self.fmtArrTextStart.text())
        self.fillColorData()


    def arrayFormatterSepSlot(self):
        self.arrayFormatter.setSep(self.fmtArrTextSep.text())
        self.fillColorData()


    def arrayFormatterEndSlot(self):
        self.arrayFormatter.setEnd(self.fmtArrTextEnd.text())
        self.fillColorData()


    def fillColorData(self) -> None:
        effectiveColor = QColorConstants.Black if self.colors.empty() else self.colors.getActive()
        
        rgb = (effectiveColor.red(), effectiveColor.green(), effectiveColor.blue())
        rgbF = (effectiveColor.redF(), effectiveColor.greenF(), effectiveColor.blueF())
        hsl = (clamp(effectiveColor.hslHue(), 0, 360) , effectiveColor.hslSaturation(), effectiveColor.lightness())
        hslF = (clamp(effectiveColor.hslHueF(), 0.0, 1.0), effectiveColor.hslSaturationF(), effectiveColor.lightnessF())

        self.intTextRGB.setText(self.arrayFormatter.format(rgb))
        self.fillGroup((self.intTextR, self.intTextG, self.intTextB), rgb, str)
        
        self.floatTextRGB.setText(self.arrayFormatter.format(list(map(lambda x: self.formatFloat(x), rgbF))))
        self.fillGroup((self.floatTextR, self.floatTextG, self.floatTextB), rgbF, self.formatFloat)

        self.hexTextRGB.setText(self.formatHex(effectiveColor.name()))
        self.fillGroup((self.hexTextR, self.hexTextG, self.hexTextB), rgb, self.formatHex)

        self.intTextHSL.setText(self.arrayFormatter.format([hsl[0], self.formatPercentage(hsl[1]), self.formatPercentage(hsl[2])]))
        self.intTextH.setText(str(hsl[0]))
        self.intTextS.setText(self.formatPercentage(hsl[1]))
        self.intTextL.setText(self.formatPercentage(hsl[2]))

        self.floatTextHSL.setText(self.arrayFormatter.format(list(map(lambda x: self.formatFloat(x), hslF))))
        self.fillGroup((self.floatTextH, self.floatTextS, self.floatTextL), hslF, self.formatFloat)


    def fillGroup(self, group, content, formatter):
        for fieldValue in zip(group, content):
            fieldValue[0].setText(formatter(fieldValue[1]))


    def formatFloat(self, num: float) -> str:
        formatted = Decimal(f'{num:.{self.fmtSpinDecPrec.value()}f}').normalize().to_eng_string()
        # Forcefully add a .0 to integral numbers
        reformatted = f'{formatted}.0' if '.' not in formatted else formatted
        
        return reformatted.replace('.', ',') if self.fmtChkDecimalsSep.isChecked() else reformatted


    def formatHex(self, num: Union[int, str]) -> str:
        noHash = self.fmtChkHexNoHash.isChecked()

        if isinstance(num, int):
            formatted = f'{num:x}'.upper()
            # Forcefully define pure black as '00'
            reformatted = '00' if formatted == '0' else formatted
            return reformatted if noHash else f'#{reformatted}'
        else:
            return (num[1:] if noHash else num).upper()


    def formatPercentage(self, num: Number) -> str:
        if self.fmtChkSLPercentage.isChecked():
            return f'{self.formatFloat(num / 255 * 100)}%'
        return self.formatFloat(num)


if __name__ == '__main__':
    app = QApplication(argv)
    win = Window()
    #win.setWindowFlags(Qt.WindowTransparentForInput)
    win.show()
    exit(app.exec())
