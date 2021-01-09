import json
import os
import re

import pandas as pd

from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QRadioButton, QDoubleSpinBox, QSpinBox, QCheckBox, QLineEdit, QTextEdit, QComboBox, \
    QTableWidget, QFileDialog

from fep_modules.config import config


class Util:
    def __init__(self):
        pass

    # 从 file 中读取数据
    def read_from_file_click(self, filepath_line2, basename=False):
        try:
            fileName, filetype = QFileDialog.getOpenFileName(None,
                                                             "Select File",
                                                             self.working_path,
                                                             "All Files (*);;Text Files (*.txt)")

            # data = read_from_file(fileName)
            if fileName:
                if basename:
                    filepath_line2.setText(os.path.basename(fileName))
                else:
                    filepath_line2.setText(fileName)

        except:
            pass

    def get_widget_state(self, widget):
        assert isinstance(widget, QObject)
        params = {}
        radio_btns = widget.findChildren(QRadioButton)
        for radio_btn in radio_btns:
            params.update({radio_btn.objectName(): radio_btn.isChecked()})
        doublespinboxes = widget.findChildren(QDoubleSpinBox)
        for spinbox in doublespinboxes:
            key = spinbox.objectName()
            params.update({key: spinbox.value()})
        spinboxes = widget.findChildren(QSpinBox)
        for spinbox in spinboxes:
            key = spinbox.objectName()
            params.update({key: spinbox.value()})
        checkboxs = widget.findChildren(QCheckBox)
        for checkbox in checkboxs:
            params.update({checkbox.objectName(): checkbox.isChecked()})
        lineEdits = widget.findChildren(QLineEdit)
        for lineedit in lineEdits:
            if 'qt_spinbox_lineedit' == lineedit.objectName():
                continue
            key = lineedit.objectName()
            value = lineedit.text()
            params.update({key: value})
        textEdits = widget.findChildren(QTextEdit)
        for textedit in textEdits:
            key = textedit.objectName()
            value = textedit.toPlainText()
            params.update({key: value})
        comboxes = widget.findChildren(QComboBox)
        for combox in comboxes:
            key = combox.objectName()
            params.update({key: combox.currentText()})
        tables = widget.findChildren(QTableWidget)
        # for combox in comboxes:
        #     key = combox.objectName()
        #     params.update({key: combox.currentText()})
        return_dic = {}
        for k, v in params.items():
            if type(v) is str:
                v = v.strip().replace("  ", " ").replace(" ", "_").lower()
            return_dic[k.strip().replace("  ", " ").replace(" ", "_").lower()] = v
        return return_dic

    # 导出参数
    def export_param(self, widget, name):
        os.makedirs(config.working_path, exist_ok=True)
        os.makedirs(os.path.join(config.working_path, 'param'), exist_ok=True)
        try:
            with open(os.path.join(config.working_path, 'param', str(name) + '.json'), 'w') as w:
                print("export_param")
                print(my_util.get_widget_state(widget))
                w.write(json.dumps(self.get_widget_state(widget), indent=4))
        except Exception as e:
            print(e)


    # 获取对应组件的相关表格信息
    def get_table_insert(self, table_widget, table_path=None, headerfunc=None):
        headers, indices, content = self.get_table_content(table_widget)
        df = self.get_table_df(table_widget)

        if table_path == None:
            return 0
        if not os.path.exists(table_path):
            return 0

        trial = open(table_path).read().strip().split("\n")
        hd = trial[0].split(',')
        rows_in = len(trial)
        cols_in = len(hd)

        if headerfunc is not None:
            headers_in = headerfunc(cols_in)
        else:
            headers_in = headers[:cols_in]

        if re.match(r'[0-9.-]+', hd[1]):
            df_in = pd.read_csv(table_path, header=None, names=headers_in)
        else:
            df_in = pd.read_csv(table_path, header=0, names=headers_in)
        print(df_in)

        for i in range(df_in.shape[0]):
            found = False
            for j in range(df.shape[0]):
                if df_in.loc[i, 'Ligand'] == df.loc[j, 'Ligand']:
                    found = True
                    for k in df_in.columns:
                        df.loc[j, k] = df_in.loc[i, k]
                    break
            if not found:
                continue

        cols = table_widget.columnCount()
        rows = table_widget.rowCount()
        for i in range(rows):
            for j in range(cols):
                table_widget.item(i, j).setText(str(df.iloc[i, j]))
        __sortingEnabled = table_widget.isSortingEnabled()
        table_widget.setSortingEnabled(False)
        table_widget.setSortingEnabled(__sortingEnabled)
        # table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # table_widget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        print(df)
        return df

    def sort_table(self, index, table_widget):
        if index == 2:
            if table_widget.table_descending:
                table_widget.sortItems(2, Qt.AscendingOrder)
            else:
                table_widget.sortItems(2, Qt.DescendingOrder)
            table_widget.table_descending = not table_widget.table_descending


    def get_table_df(self, table_widget, index=False):
        headers, indices, content = self.get_table_content(table_widget)
        if index:
            df = pd.DataFrame(content, columns=headers, index=indices)
        else:
            df = pd.DataFrame(content, columns=headers)
        return df

    def get_table_content(self, table_widget):
        cols = table_widget.columnCount()
        rows = table_widget.rowCount()

        headers = []
        indices = []
        content = []
        for i in range(cols):
            headers.append(table_widget.horizontalHeaderItem(i).text())
        for i in range(rows):
            indices.append(table_widget.verticalHeaderItem(i).text())

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(table_widget.item(i, j).text())
            content.append(row)
        return headers, indices, content

my_util = Util()