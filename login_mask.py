import sys

from PyQt5 import QtWidgets
from PyQt5.Qt import *

from fep_modules.login_dialog import Ui_login_dialog
from fep_modules.login_dialog_impl import MyLoginDialog
from fep_modules.login_impl import MyLogin


class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('background:rgba(0,0,0,102);')
        self.setAttribute(Qt.WA_DeleteOnClose)

    def show(self):
        """重写show，设置遮罩大小与parent一致"""
        if self.parent() is None:
            return
        parent_rect = self.parent().geometry()
        self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
        super().show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = MyLogin()
    login.show()
    mask = MaskWidget(login)
    dialog = MyLoginDialog()

    mask.show()
    result = dialog.exec()
    print(result)
    mask.close()
    sys.exit(app.exec_())

