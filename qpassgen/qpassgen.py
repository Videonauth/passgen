#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
############################################################################
#
# qpassgen.py
#
############################################################################
#
# Author: Videonauth <videonauth@googlemail.com>
# Date: 04.07.2016
# Purpose:
#     Generate a randomized password of given length, GUI module.
# Written for: Python 3.5.1
#
############################################################################

# import passgen
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class PassGenUI(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)
        self.center()
        self.setWindowTitle("QPassGen 0.0.6")
        self.show()

    def center(self):
        rectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(centerpoint)
        self.move(rectangle.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassGenUI()
    sys.exit(app.exec_())
