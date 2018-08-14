#!/usr/bin/python

import sys
from src.ui.mainwindow import MainWindow

from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
