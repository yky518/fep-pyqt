import json
import os
import pickle
import shutil
import sys

import pandas as pd

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QMessageBox, QWidget

from FEprep import pert_graph
from FEprep.utils import morph_util
from QtExtension.QTableOptWidget import QTableOptWidget, QAbstractItemView
from fep_modules.preparation import Ui_preparation

from fep_modules.config import config
from fep_modules.util import my_util


class MyPreparation(QtWidgets.QWidget, Ui_preparation):
    def __init__(self, tab_pert, tab_widget):
        super(MyPreparation, self).__init__()
        self.setupUi(self)
        self.tabWidget = tab_widget

        self.graphics_pertGraph = tab_pert.graphics_pertGraph
        self.ligands_file = ''

        self.peoject_button.clicked.connect(lambda x: (self.get_chkp_dir_click(self.project_line),
                                                       self.change_working_path(self.project_line.text())))
        self.job_button.clicked.connect(lambda x: (self.get_chkp_dir_click(self.job_line),
                                                   self.change_working_path(self.job_line.text())))
        self.protein_button.clicked.connect(lambda x: self.read_from_file_click(self.protein_file))

        self.ligand_button.clicked.connect(lambda x: (self.get_ligands(),  # 生成csv表格文件保存在本地
                                                      tab_pert.get_ligand_table(table_path=self.ligands_file),
                                                      # perturbation页表格生成
                                                      self.get_table(self.tableOpt_ligFiles, self.prepare_headers,
                                                                     table_path=self.ligands_file)))  # 当前页表格生成
        self.button_next_prep.clicked.connect(lambda x: (my_util.export_param(self, "preparation"),
                                                         self.tabWidget.setCurrentIndex(
                                                             self.tabWidget.currentIndex() + 1),
                                                         self.prepara()))

        self.button_dGImport.clicked.connect(lambda x: self.import_affinity_data())
        self.hermite_button.clicked.connect(lambda x: (print(self.tableOpt_ligFiles.currentRow())))

        self.tableOpt_ligFiles = QTableOptWidget(button_types=['del'])
        self.tableOpt_ligFiles.setObjectName("tableOpt_ligFiles")
        self.tableOpt_ligFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableOpt_ligFiles.setSelectionMode(QAbstractItemView.MultiSelection)

        self.table_layout.addWidget(self.tableOpt_ligFiles)
        self.tableOpt_ligFiles.set_table_and_buttons_with_df(pd.DataFrame(
            {'Name': [], 'Crystal Structure': [], 'Exp. Affinity\n(kcal/mol)': [], 'Exp. Error\n(kcal/mol)': [],
             'Opts': []}))

    # 导入exp数据
    def import_affinity_data(self):
        fileName, filetype = QFileDialog.getOpenFileName(None,
                                                         "Select File",
                                                         config.working_path,
                                                         "All Files (*);;")
        headers = ['Ligand', 'Crystal Structure', 'Exp. Affinity (kcal/mol)', 'Exp. Error (kcal/mol)', 'Weight']
        # 将 fileName 和 ligand file 结合
        if fileName:
            try:
                count = 0
                f = open(fileName)
                config.has_exp_data = fileName
                # tmp_dic = {}
                # # 获取ligands 的实验数据
                # for line in f:
                #     if count == 0:
                #         count += 1
                #         continue
                #     tmp_list = line.strip().split(',')
                #     tmp_dic[tmp_list[0]] = tmp_list
                # # 将实验数据和本地数据结合
                # with open(self.ligands_file, 'w') as w:
                #     w.write(",".join(self.ligands_headers) + '\n')
                #     for tmp_ligands in self.ligands:
                #         tmp_ligands = tmp_ligands.split('.')[0]
                #         w.write(",".join(list(map(str, [tmp_ligands,
                #                           tmp_dic.get(tmp_ligands, [0, 0, 0])[1],
                #                                         tmp_dic.get(tmp_ligands, [0, 0, 0])[2], '1']))) + '\n')

                df = self.get_table_insert(table_widget=self.tableWidget, table_path=fileName,
                                           headerfunc=config.determine_ligand_header)
                df.to_csv(self.ligands_file, index=False, float_format="%.3f")
                config.graph_doe, config.data_pos = pert_graph.graph_DoE_init(simmat=config.simmat,
                                                                              lig_names=config.ligands,
                                                                              has_exp_data=config.has_exp_data)

            except Exception as e:
                print(e)

    # 将文件浏览插件获取的文件目录的值给对应的文本输入框
    def get_chkp_dir_click(self, chkp_dir_line):
        try:
            foldername = QFileDialog.getExistingDirectory(None,
                                                          'Select Folder',
                                                          '')
            if foldername:
                foldername = foldername.replace("\\", "/")
                chkp_dir_line.setText(foldername)
            # self.parent().save_dir.update(foldername, )
            # self.logger.info('set {} as job folder'.format(foldername))
        except Exception as e:
            # self.logger.error('fail to set job folder')
            print(e)
            pass

    # 改变当前的工作目录
    def change_working_path(self, new_path):
        if not new_path:
            return 0
        config.working_path = new_path
        os.makedirs(os.path.join(new_path), exist_ok=True)

    # 从 file 中读取数据
    def read_from_file_click(self, filepath_line2, basename=False):
        try:
            fileName, filetype = QFileDialog.getOpenFileName(None,
                                                             "Select File",
                                                             config.working_path,
                                                             "All Files (*);;Text Files (*.txt)")

            # data = read_from_file(fileName)
            if fileName:
                if basename:
                    filepath_line2.setText(os.path.basename(fileName))
                else:
                    filepath_line2.setText(fileName)

        except:
            pass

    # 获取对应组件的相关表格信息
    def get_table(self, table_widget, table_path=None):
        headers = ['Name', 'Crystal\nStructure', 'Exp. Affinity (kcal/mol)', 'Exp. Error (kcal/mol)',
                   'Opts']
        if table_path == None:
            return 0
        if not os.path.exists(table_path):
            return 0
        data = open(table_path).read().strip().split("\n")
        # if not headers:
        #     headers = data[0].split(',')
        row = len(data) - 1
        column = len(headers)
        table_widget.setColumnCount(column)
        table_widget.setRowCount(row)
        # # 确定表头
        # for i in range(column):
        #     item = QtWidgets.QTableWidgetItem()
        #     item.setText(headers[i])
        #     table_widget.setHorizontalHeaderItem(i, item)
        # # 确定行index
        # for i in range(row):
        #     item = QtWidgets.QTableWidgetItem()
        #     item.setText(str(i))
        #     table_widget.setVerticalHeaderItem(i, item)
        # 确定数据内容
        data = data[1:]
        for i in range(row):
            tmp_data = data[i].split(',')
            for j in range(column):
                item = QtWidgets.QTableWidgetItem()
                item.setText(tmp_data[j])
                table_widget.setItem(i, j, item)
        __sortingEnabled = table_widget.isSortingEnabled()
        table_widget.setSortingEnabled(False)
        table_widget.setSortingEnabled(__sortingEnabled)
        # table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # table_widget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

    # 获取目录中的ligand 文件
    def get_ligands(self):
        df = self.tableOpt_ligFiles.get_table_df()
        config.ligands_path = list(df['files'])
        config.ligands = list(df['name'])
        config.ligands_id = list(df['id'])
        try:
            lig_files = QFileDialog.getOpenFileNames(None, "Select Ligand Files")[0]
            lig_names, file_per_lig, lig_ids = morph_util.lig_files_to_names(lig_files)
            config.ligands += lig_names
            config.ligands_path += file_per_lig
            config.ligands_id += lig_ids
        # try:
        #     foldername = QFileDialog.getExistingDirectory(None,
        #                                                   'Select Folder',
        #                                                   '')
        #     if foldername:
        #         foldername = foldername.replace("\\", "/")
        #         self.ligands_path = foldername
        #     else:
        #         return 0
        # self.parent().save_dir.update(foldername, )
        # self.logger.info('set {} as job folder'.format(foldername))
        except Exception as e:
            # self.logger.error('fail to set job folder')
            print(e)
            pass
        # for line in os.listdir(self.ligands_path):
        #     if ".mol" in line:
        #         self.ligands.append(line.strip())
        # 将当前的ligands 信息输入到ligands file
        self.ligands_file = os.path.join(config.working_path, 'ligands.csv')
        print(self.ligands_file)
        with open(self.ligands_file, 'w') as w:
            w.write(",".join(config.ligands_headers) + '\n')
            for tmp_ligand in config.ligands:
                w.write(",".join([tmp_ligand, 'True', '0', '0', '1']) + '\n')

    # 进行preparation操作
    def prepara(self):
        try:
            param = json.loads(open(os.path.join(config.working_path, "param", "preparation.json")).read())
            # 复制配体文件
            # ligand_dir = self.ligands_path  # your directory to /FEP_local_test, e.g. "~/FEP_local_test"
            molfiles = config.ligands_path
            mols_in_table = self.tableOpt_ligFiles.get_table_df()

            imgfiles = pert_graph.ligs_copy_allformat(molfiles=list(mols_in_table['files']),
                                                      ids=list(mols_in_table['id']),
                                                      job_dir=config.working_path,
                                                      lignames=list(mols_in_table['name']))
            # imgfiles = [img.rstrip("png")+"svg" for img in imgfiles]
            self.graphics_pertGraph.clear_graph()
            self.graphics_pertGraph.init_graph(graph_a=None, names=list(mols_in_table['name']),
                                               imgs=imgfiles)
            config.simmat = pert_graph.calc_simmat(
                filenames=[os.path.splitext(imgfile)[0] + ".mol" for imgfile in imgfiles])
            config.graph_doe, config.data_pos = pert_graph.graph_DoE_init(simmat=config.simmat,
                                                                          lig_names=config.ligands,
                                                                          initialize="no")
            with open(os.path.join(config.working_path, "ligands", "graph_doe.pickle"), 'wb') as pfile:
                pickle.dump(config.graph_doe, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump(config.simmat, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump('tanimoto_fingerprint', pfile, pickle.HIGHEST_PROTOCOL)
            # if ligand_dir != self.working_path:
            #     for tmp_file in molfiles:
            #         shutil.copy(tmp_file, self.working_path)

            # self.comboBox_update_ligands(comboBox=self.combo_ligStart)
            # self.comboBox_update_ligands(comboBox=self.combo_ligEnd)
            # 改变 蛋白文件，进行抽取出文件名
            param['protein_file_from'] = param['protein_file']
            param['protein_file'] = param['protein_file_from'].split("/")[-1]
            # 复制protein文件
            protein_file = param['protein_file_from']
            if os.path.exists(protein_file) and not os.path.exists(
                    os.path.join(config.working_path, param['protein_file'])):
                shutil.copy(protein_file, config.working_path)
            with open(os.path.join(config.working_path, "param", "preparation.json"), 'w') as w:
                w.write(json.dumps(param, indent=4))
            QMessageBox.information(QWidget(), 'Success', 'Get param.json')
        except Exception as e:
            QMessageBox.critical(QWidget(), 'Error', str(e))

    def comboBox_update_ligands(self, comboBox):
        comboBox.clear()
        with open(os.path.join(config.working_path, "ligands", "lignames.pickle"), 'rb') as pfile:
            lig_names = pickle.load(pfile)
        for ligname in lig_names:
            comboBox.addItem(ligname)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_mapping = MyPreparation()
    my_mapping.show()
    sys.exit(app.exec_())
