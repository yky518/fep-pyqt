import json
import os

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog

from fep_modules.login_dialog import Ui_login_dialog


class MyLoginDialog(QtWidgets.QDialog, Ui_login_dialog):
    def __init__(self):
        super(MyLoginDialog, self).__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.login)
        self.cancel_button.clicked.connect(self.cancel)
        self.config_button.clicked.connect(lambda x: self.read_from_file_click(self.config_edit))
        self.config_data = None


    def cancel(self):
        self.usernameLineEdit.setText('')
        self.passwordLineEdit.setText('')
        self.configTextBrowser.setText('')

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

                self.configTextBrowser.setText(config)
            # data = read_from_file(fileName)
            if fileName:
                if basename:
                    filepath_line2.setText(os.path.basename(fileName))
                else:
                    filepath_line2.setText(fileName)

        except:
            pass

    def login(self):
        # try:
        #     self.username = self.usernameLineEdit.text()
        #     self.config_data['username'] = self.username
        #     self.update_config()
        #     avail_user_list = ["zhangyuzhi", "changjunhan", "DPTech", "Hengrui"]
        #     if self.username not in avail_user_list:
        #         QMessageBox.information(QWidget(), 'Failure',
        #                                 "Your username %s is not in available user list !" % self.username)
        #         raise RuntimeError("Your username %s is not in available user list !" % self.username)
        #     QMessageBox.information(QWidget(), 'Success', 'loging success')
        #     # 如果登录成功 获取相关信息
        #     # self.get_job_info()
        #     self.close()
        #     return 1
        # except Exception as e:
        #     print(e)
        # return 0
        self.accept()

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
