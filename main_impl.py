import sys

from PyQt5 import QtWidgets

from fep_modules.main import Ui_Dialog


class MyMain(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_mapping = MyMain()
    my_mapping.show()
    sys.exit(app.exec_())