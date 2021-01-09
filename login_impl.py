import json
import os
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog, QPushButton, QHBoxLayout

from fep_modules.login import Ui_MyLogin

from PyQt5.QtCore import QFileInfo, QSize, QCoreApplication, Qt
from PyQt5.QtGui import QIcon

_translate = QCoreApplication.translate


class MyLogin(QtWidgets.QWidget, Ui_MyLogin):
    def __init__(self):
        super(MyLogin, self).__init__()
        self.setupUi(self)
        self.config = "config.json"
        self.config_data = {}
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(lambda x: self.read_from_file_click(self.lineEdit))
        self.table_headers = [
            'JobID',
            'JobName',
            'Process',
            'Running Time',
            'Cost',
            'Status',
            'Ops'
        ]

        self.table_data = [
            {
                'JobID': '1231',
                'JobName': 'test',
                'Process': '60/99',
                'Running': '11:15:80',
                'Cost': '￥300',
                'Status': 'Running',
            },
            {
                'JobID': '1111',
                'JobName': 'test',
                'Process': '60/99',
                'Running': '11:15:80',
                'Cost': '￥300',
                'Status': 'Running',
            }
        ]
        self.get_table(self.tableWidget_job, self.table_data)

    def get_table(self, tableWidget, table_data):
        print("get table")

        tableWidget.setColumnCount(len(self.table_headers))
        tableWidget.setRowCount(len(table_data))

        # 数据填充
        row = 0
        for row_data in table_data:
            column = 0

            root = QFileInfo('play.png').absolutePath()
            print('根目录' + root)
            icon1 = QIcon(root + '/fep_modules/imgs/play.png')
            icon2 = QIcon(root + '/fep_modules/imgs/edit.png')
            icon3 = QIcon(root + '/fep_modules/imgs/download.png')

            for key in row_data.keys():
                item = QtWidgets.QTableWidgetItem()
                item.setText(row_data[key])
                item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(row, column, item)
                column += 1

            cell_widget = QWidget()
            cell_widget.setObjectName("cell_widget")
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setObjectName('layout')

            button1 = QPushButton()
            button1.setObjectName('button1')
            button1.setStyleSheet('''
                QPushButton {
                    border: none;
                    padding: 2px;
                }
                QPushButton:pressed{
                    background-color: #000000;
                }
            ''')
            button1.setIcon(icon1)
            button1.clicked.connect(lambda: (print('button1')))

            button2 = QPushButton()
            button2.setObjectName('button2')

            button2.setStyleSheet('''
                QPushButton {
                    border: none;
                    padding: 2px;
                }
                QPushButton:pressed{
                    background-color: #000000;
                }
            ''')
            # button2.setIconSize(QSize(96,96))

            button2.setIcon(icon2)
            button2.clicked.connect(lambda: (print('button2')))

            button3 = QPushButton()
            button3.setObjectName('button3')
            button3.setStyleSheet('''
                QPushButton {
                    border: none;
                    padding: 2px;
                }
                QPushButton:pressed{
                    background-color: #000000;
                }
            ''')
            button3.setIcon(icon3)
            button3.clicked.connect(lambda: (print('button3')))

            layout.addWidget(button1)
            layout.addWidget(button2)
            layout.addWidget(button3)

            cell_widget.setLayout(layout)
            tableWidget.setCellWidget(row, column, cell_widget)
            row += 1

    # 实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushButton_click(self):
        self.textEdit.setText("你点击了按钮")

    def read_from_file_click(self, filepath_line2, basename=False):
        try:
            fileName, filetype = QFileDialog.getOpenFileName(None,
                                                             "Select File", '.',
                                                             "All Files (*);;Text Files (*.txt)")

            print(fileName)
            filepath = os.path.basename(fileName)
            print(filepath)
            print(os.path.dirname(fileName))

            with open(fileName, 'r') as conf_file:
                print("open")
                config = conf_file.read()
                self.config_data = json.loads(config)

                self.textBrowser.setText(config)
            # data = read_from_file(fileName)
            if fileName:
                if basename:
                    filepath_line2.setText(os.path.basename(fileName))
                else:
                    filepath_line2.setText(fileName)

        except:
            pass

    def login(self):
        try:
            self.username = self.usernameLineEdit.text()
            self.config_data['username'] = self.username
            self.update_config()
            avail_user_list = ["zhangyuzhi", "changjunhan", "DPTech", "Hengrui"]
            if self.username not in avail_user_list:
                QMessageBox.information(QWidget(), 'Failure',
                                        "Your username %s is not in available user list !" % self.username)
                raise RuntimeError("Your username %s is not in available user list !" % self.username)
            QMessageBox.information(QWidget(), 'Success', 'loging success')
            # 如果登录成功 获取相关信息
            self.get_job_info()
            return 1
        except Exception as e:
            print(e)
        return 0

    def update_config(self):
        with open('../config.json', 'w') as w:
            w.write(json.dumps(self.config_data, indent=4))

    def get_job_info(self):
        if self.username == '':
            return 0
        url_0 = self.base_url + 'get_username_info?username=' + self.username
        try:
            res = requests.get(url_0)
            return_data = res.json()['data']
            print(return_data)
        except Exception as e:
            print(e)
            return 0
        if len(return_data) == 0:
            return 0
        count = 0
        new_id = 0
        self.combo_job.clear()
        self.combo_job.addItem(' ')
        for line in return_data:
            new_id = line['id']
            self.combo_job.addItem(str(line['id']))
            count += 1
        self.job_id = new_id
        return 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyLogin()
    my_pyqt_form.show()
    sys.exit(app.exec_())
