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

from decimal import Decimal
from pathlib import Path
from typing import Optional, Union, Iterable, Callable, Any

from PySide6.QtGui import (QGuiApplication, QColorConstants, QColor, QBrush, QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsRectItem, QGraphicsScene, QLineEdit)
from PySide6.QtCore import (QLibraryInfo, QTranslator, QLocale)

from app.ui.main_window import Ui_MainWindow
from app.utils.Collections import (CollectionFormatter, ActiveList)
from app.utils.Maths import clamp
from app.widgets.ColorPickers import (PixelColorPicker, RegionColorPicker)

import cs3_rc

class Cs3MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window widget of the cs3 application.
    """
    def __init__(self):
        super(Cs3MainWindow, self).__init__()
        # UI setup
        self.setupUi(self)
        # Class members
        self.arrayFormatter = CollectionFormatter(
            self.fmtArrTextStart.text(),
            self.fmtArrTextSep.text(),
            self.fmtArrTextEnd.text()
        )
        self.SAMPLE_DIM = 200
        self.sampleScene = QGraphicsScene(0, 0, self.SAMPLE_DIM, self.SAMPLE_DIM)
        self.sampleItem = QGraphicsRectItem(0, 0, self.SAMPLE_DIM, self.SAMPLE_DIM)
        self.colors = ActiveList()
        # Slots setup
        self.sampleBtn.clicked.connect(self.sample_screen_slot)
        self.sampleNavBtnPrev.clicked.connect(self.nav_previous_sample_slot)
        self.sampleNavBtnNext.clicked.connect(self.nav_next_sample_slot)
        self.fmtSpinDecPrec.valueChanged[int].connect(lambda x: self.fill_color_data())
        self.fmtChkDecimalsSep.stateChanged[int].connect(lambda x: self.fill_color_data())
        self.fmtChkHexNoHash.stateChanged[int].connect(lambda x: self.fill_color_data())
        self.fmtChkSLPercentage.stateChanged[int].connect(lambda x: self.fill_color_data())
        self.fmtArrTextStart.textChanged[str].connect(self.array_formatter_start_slot)
        self.fmtArrTextSep.textChanged[str].connect(self.array_formatter_sep_slot)
        self.fmtArrTextEnd.textChanged[str].connect(self.array_formatter_end_slot)
        self.intBtnCopyR.clicked.connect(lambda x: self.field_to_clipboard(self.intTextR))
        self.intBtnCopyG.clicked.connect(lambda x: self.field_to_clipboard(self.intTextG))
        self.intBtnCopyB.clicked.connect(lambda x: self.field_to_clipboard(self.intTextB))
        self.intBtnCopyRGB.clicked.connect(lambda x: self.field_to_clipboard(self.intTextRGB))
        self.floatBtnCopyR.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextR))
        self.floatBtnCopyG.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextG))
        self.floatBtnCopyB.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextB))
        self.floatBtnCopyRGB.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextRGB))
        self.hexBtnCopyR.clicked.connect(lambda x: self.field_to_clipboard(self.hexTextR))
        self.hexBtnCopyG.clicked.connect(lambda x: self.field_to_clipboard(self.hexTextG))
        self.hexBtnCopyB.clicked.connect(lambda x: self.field_to_clipboard(self.hexTextB))
        self.hexBtnCopyRGB.clicked.connect(lambda x: self.field_to_clipboard(self.hexTextRGB))
        self.intBtnCopyH.clicked.connect(lambda x: self.field_to_clipboard(self.intTextH))
        self.intBtnCopyS.clicked.connect(lambda x: self.field_to_clipboard(self.intTextS))
        self.intBtnCopyL.clicked.connect(lambda x: self.field_to_clipboard(self.intTextL))
        self.intBtnCopyHSL.clicked.connect(lambda x: self.field_to_clipboard(self.intTextHSL))
        self.floatBtnCopyH.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextH))
        self.floatBtnCopyS.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextS))
        self.floatBtnCopyL.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextL))
        self.floatBtnCopyHSL.clicked.connect(lambda x: self.field_to_clipboard(self.floatTextHSL))
        # Visual init
        self.sampleItem.setBrush(QBrush(QColorConstants.Black))
        self.sampleScene.addItem(self.sampleItem)
        self.sampleDisplay.setScene(self.sampleScene)
        self.sampleDisplay.show()

    @staticmethod
    def field_to_clipboard(field: QLineEdit) -> None:
        """
        Replaces the content of the clipboard with the content of the line edit.
        """
        QGuiApplication.clipboard().setText(field.text())

    def sample_screen_slot(self) -> None:
        """
        Creates and runs a color picker widget.
        """
        if self.selectionConfigRadSingle.isChecked():
            cp = PixelColorPicker(self)
        else:
            cp = RegionColorPicker(self)
        cp.colorSample.connect(self.add_new_color)

    def nav_previous_sample_slot(self) -> None:
        """
        Loads and displays the previous color sample.
        """
        self.colors.move_to_previous()
        self.refresh_color_ui()

    def nav_next_sample_slot(self) -> None:
        """
        Loads and displays the next color sample.
        """
        self.colors.move_to_next()
        self.refresh_color_ui()

    def add_new_color(self, color: Optional[QColor]) -> None:
        """
        Stores and displays a new color sample.
        """
        if color is None:
            return
        self.colors.append(color)
        self.refresh_color_ui()

    def refresh_color_ui(self) -> None:
        """
        Updates all UI elements related to the color sample.
        """
        self.update_sample_navigation()
        self.fill_color_data()
        self.sampleItem.setBrush(self.colors.get_active())

    def update_sample_navigation(self) -> None:
        """
        Enables and disables the navigation buttons depending on
        the availability of neighbouring color samples to the active.
        """
        self.sampleNavBtnPrev.setEnabled(not self.colors.at_start())
        self.sampleNavBtnNext.setEnabled(not self.colors.at_end())

    def array_formatter_start_slot(self) -> None:
        """
        Changes the starting symbols of the array formatter and refresh the data fields.
        """
        self.arrayFormatter.set_start(self.fmtArrTextStart.text())
        self.fill_color_data()

    def array_formatter_sep_slot(self) -> None:
        """
        Changes the separator symbols of the array formatter and refresh the data fields.
        """
        self.arrayFormatter.set_sep(self.fmtArrTextSep.text())
        self.fill_color_data()

    def array_formatter_end_slot(self) -> None:
        """
        Changes the ending symbols of the array formatter and refresh the data fields.
        """
        self.arrayFormatter.set_end(self.fmtArrTextEnd.text())
        self.fill_color_data()

    def fill_color_data(self) -> None:
        """
        Computes and display all text info about the current color sample.
        """
        effective_color = QColorConstants.Black if self.colors.empty() else self.colors.get_active()

        rgb = (effective_color.red(), effective_color.green(), effective_color.blue())
        rgb_f = (effective_color.redF(), effective_color.greenF(), effective_color.blueF())
        hsl = (clamp(effective_color.hslHue(), 0, 360), effective_color.hslSaturation(), effective_color.lightness())
        hsl_f = (
            clamp(effective_color.hslHueF(), 0.0, 1.0), effective_color.hslSaturationF(), effective_color.lightnessF()
        )

        self.intTextRGB.setText(self.arrayFormatter.format(rgb))
        self.fill_group((self.intTextR, self.intTextG, self.intTextB), rgb, str)

        self.floatTextRGB.setText(self.arrayFormatter.format(list(map(lambda x: self.format_float(x), rgb_f))))
        self.fill_group((self.floatTextR, self.floatTextG, self.floatTextB), rgb_f, self.format_float)

        self.hexTextRGB.setText(self.format_hex(effective_color.name()))
        self.fill_group((self.hexTextR, self.hexTextG, self.hexTextB), rgb, self.format_hex)

        self.intTextHSL.setText(
            self.arrayFormatter.format([hsl[0], self.format_percentage(hsl[1]), self.format_percentage(hsl[2])]))
        self.intTextH.setText(str(hsl[0]))
        self.intTextS.setText(self.format_percentage(hsl[1]))
        self.intTextL.setText(self.format_percentage(hsl[2]))

        self.floatTextHSL.setText(self.arrayFormatter.format(list(map(lambda x: self.format_float(x), hsl_f))))
        self.fill_group((self.floatTextH, self.floatTextS, self.floatTextL), hsl_f, self.format_float)

    @staticmethod
    def fill_group(fields: Iterable, content: Iterable, formatter: Callable[[Any], str]) -> None:
        """
        Injects content formatted using the provided formatter into text-editable fields in order.
        """
        for field_content_tuple in zip(fields, content):
            field_content_tuple[0].setText(formatter(field_content_tuple[1]))

    def format_float(self, num: Union[int , float]) -> str:
        """
        Stringify a number to a float with a UI-defined precision, UI-defined separator
        and no trailing 0 unless it's an integral number
        """
        formatted = Decimal(f'{num:.{self.fmtSpinDecPrec.value()}f}').normalize().to_eng_string()
        # Forcefully add a .0 to integral numbers
        reformatted = f'{formatted}.0' if '.' not in formatted else formatted

        return reformatted.replace('.', ',') if self.fmtChkDecimalsSep.isChecked() else reformatted

    def format_hex(self, num: Union[int, str]) -> str:
        """
        Stringify a base 10 number into its hexadecimal representation with an optional UI-defined hash prefix.
        """
        no_hash = self.fmtChkHexNoHash.isChecked()

        if isinstance(num, int):
            formatted = f'{num:x}'.upper()
            # Forcefully define pure black as two zeros
            reformatted = '00' if formatted == '0' else formatted
            return reformatted if no_hash else f'#{reformatted}'
        else:
            return (num[1:] if no_hash else num).upper()

    def format_percentage(self, num: Union[int, float]) -> str:
        """
        Stringify a number into either a float
        """
        if self.fmtChkSLPercentage.isChecked():
            return f'{self.format_float(num / 255 * 100)}%'
        return str(num)


class Cs3Runner():
    @staticmethod
    def run(argv) -> QApplication:
        app = QApplication(argv)

        base_lang_path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        custom_lang_path = ':lang/translations/'
        # Setup core language
        translator = QTranslator(app)
        if translator.load(QLocale.system(), 'qtbase', '_', base_lang_path):
            app.installTranslator(translator)
        # Add custom translations
        translator = QTranslator(app)
        if QLocale.system().language() == QLocale.French and translator.load('fr', custom_lang_path):
            app.installTranslator(translator)

        win = Cs3MainWindow()
        win.show()
        return app.exec()
