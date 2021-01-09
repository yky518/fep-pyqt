import json
import os
import pickle
import re
import shutil
import sys

import pandas as pd
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QVBoxLayout, QFileDialog, QWidget, QMessageBox, QAbstractItemView

from FEprep import pert_top, pert_graph
from QtExtension.QGraphWidget import QGraphWidget
from PyQt5.QtCore import Qt, QFileInfo

from fep_modules.util import my_util

from PyQt5 import QtWidgets

from fep_modules.config import config
from fep_modules.perturbation import Ui_Perturbation


class MyPerturbation(QtWidgets.QWidget, Ui_Perturbation):
    def __init__(self, tab_mapping, tabWidget):
        super(MyPerturbation, self).__init__()
        self.setupUi(self)

        self.tab_mapping = tab_mapping
        self.tabWidget = tabWidget
        self.graphics_pertGraph = QGraphWidget()
        self.graphics_pertGraph.setObjectName("graphicsView")
        self.tabWidget = tabWidget
        self.tableWidget_pairs.table_descending = True
        self.tableWidget_pairs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.graph_layout.setStretch(2, 18)
        self.graph_layout.addWidget(self.graphics_pertGraph)
        self.button_graphAddEdge.clicked.connect(self.graph_add_edge)
        self.button_graphDelEdge.clicked.connect(self.graph_del_edge)
        self.button_graphUndo.clicked.connect(self.graphics_pertGraph.undoEdge)
        self.button_graphRedo.clicked.connect(self.graphics_pertGraph.redoEdge)
        self.button_next_pert.clicked.connect(lambda x: (self.update_ligandInfo(),
                                                              self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1),
                                                              ))

        self.button_graphGen.clicked.connect(lambda x: (my_util.export_param(self.tab_ligs, 'ligands'), self.generate()))
        self.button_graphLoad.clicked.connect(lambda x: (self.get_graph()))


    def update_ligandInfo(self):
        df = my_util.get_table_df(table_widget=self.tableWidget_ligands)
        print(df)
        pert_graph.update_ligs_info(job_dir=config.working_path, lignames=list(df['Ligand']), is_crystal=list(df['Crystal Structure']))


    def get_graph(self):
        job_dir = config.working_path
        # df = self.tableOpt_ligFiles.get_table_df()
        # self.ligands_path = list(df['files'])
        # self.ligands = list(df['name'])
        # self.ligands_id = list(df['id'])
        try:
            pair_file, filetype = QFileDialog.getOpenFileName(None, "Select Graph txt")
            pairs = pd.read_csv(pair_file, header=None, names=['A', 'B'], delim_whitespace=True, comment=";").astype(
                str)
            config.pairs = pairs.values.tolist()
            print(config.pairs)
            pert_list = [config.pairs[i][0] + "~" + config.pairs[i][1] for i in range(len(config.pairs))]

            for pert in pert_list:
                config.graph_doe.add_selection(pert)

            png_files = [os.path.join(config.working_path, "ligands", lig, "ligand.png") for lig in config.ligands]

            lst, pert_names = config.graph_doe.print_chosen(combine=False, print_fix=False)
            print(pert_names)
            graph_a = pert_graph.graph_DoE_readout(lst=lst, data_pos=config.data_pos,
                                                   simmat=pert_graph.inv_simmat(config.simmat))
            print(graph_a)
            pert_graph.draw_and_find_cycle(workdir=os.path.join(config.working_path, "ligands"), lig_names=config.ligands,
                                           graph_a=graph_a, png_files=png_files)

            with open(os.path.join(config.working_path, "ligands", "graph_doe.pickle"), 'wb') as pfile:
                pickle.dump(config.graph_doe, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump(graph_a, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump('tanimoto_fingerprint', pfile, pickle.HIGHEST_PROTOCOL)

            self.graphics_pertGraph.clear_graph()
            self.graphics_pertGraph.init_graph(graph_a=graph_a, names=config.ligands, imgs=png_files)

            # self.get_table(self.tableWidget_cycles, table_path=os.path.join(self.working_path, "ligands", "cycles.csv"),
            #                headers=self.cycles_headers)
            self.get_pair_table(self.tableWidget_pairs, table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            self.get_pair_table(self.tab_mapping.tableWidget, table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            # self.comboBox_update_pairs(self.combo_select_pair)
            # self.comboBox_update_pairs(self.combo_select_pair_anal)

            pert_names = ",\n".join(pert_list)

            os.chdir(os.path.join(job_dir, "ligands"))

            self.update_pert_map_setup(pert_names)
            self.update_pert_map_regen(pert_names)
            self.update_pert_top_setup(pert_names)

            pert_top.FEprep("pert_map_setup.in")
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
        print(config.pairs)


    def graph_add_edge(self):
        print("add edge")
        job_dir = config.working_path
        edge_lst = self.graphics_pertGraph.addEdge()
        if len(edge_lst) != 0:
            edge_txt = edge_lst[0] + "~" + edge_lst[1]
            # self.graph_do这是个啥？
            config.graph_doe.add_selection(edge_txt)
            self.pairs.append(edge_lst)
            pert_list = [self.pairs[i][0] + "~" + self.pairs[i][1] for i in range(len(self.pairs))]
            pert_names = ",\n".join(pert_list)

            os.chdir(os.path.join(job_dir, "ligands"))
            self.update_pert_map_setup(pert_names)
            self.update_pert_map_regen(edge_txt)
            self.update_pert_top_setup(pert_names)

            pert_top.FEprep("pert_map_regen.in")

    def graph_del_edge(self):
        job_dir = config.working_path
        edge_lst = self.graphics_pertGraph.deleteEdge()
        if len(edge_lst) != 0:
            edge_txt = edge_lst[0] + "~" + edge_lst[1]
            if os.path.exists(os.path.join(job_dir, "perturbations", edge_txt)):
                shutil.rmtree(os.path.join(job_dir, "perturbations", edge_txt))
            config.graph_doe.del_selection(edge_txt)
            config.pairs.pop(config.pairs.index(edge_lst))
            pert_list = [config.pairs[i][0] + "~" + config.pairs[i][1] for i in range(len(config.pairs))]
            pert_names = ",\n".join(pert_list)

            os.chdir(os.path.join(job_dir, "ligands"))
            self.update_pert_map_setup(pert_names)
            self.update_pert_map_regen(edge_txt)
            self.update_pert_top_setup(pert_names)

    def export_param(self, widget, name):
        os.makedirs(config.working_path, exist_ok=True)
        os.makedirs(os.path.join(config.working_path, 'param'), exist_ok=True)
        try:
            with open(os.path.join(config.working_path, 'param', str(name) + '.json'), 'w') as w:
                w.write(json.dumps(my_util.get_widget_state(widget), indent=4))
        except Exception as e:
            print(e)

    def get_graph_folder(self):
        job_dir = config.working_path
        # df = self.tableOpt_ligFiles.get_table_df()
        # self.ligands_path = list(df['files'])
        # self.ligands = list(df['name'])
        # self.ligands_id = list(df['id'])
        try:
            foldername = QFileDialog.getExistingDirectory(None,
                                                          'Select Perturbations Folder',
                                                          '')
            if foldername:
                foldername = foldername.replace("\\", "/")
            pkl = os.path.join(foldername, "pertnames.pickle")
            if os.path.exists(pkl):
                with open(pkl, 'rb') as pfile:
                    pert_list = pickle.load(pfile)
            else:
                for root, dirs, files in os.walk(foldername):
                    pert_list = dirs
                    break
            config.pairs = [pert.split('~') for pert in pert_list]

            for pert in pert_list:
                config.graph_doe.add_selection(pert)

            png_files = [os.path.join(config.working_path, "ligands", lig, "ligand.png") for lig in self.ligands]

            lst, pert_names = config.graph_doe.print_chosen(combine=False, print_fix=False)
            print(pert_names)
            graph_a = pert_graph.graph_DoE_readout(lst=lst, data_pos=config.data_pos, simmat=pert_graph.inv_simmat(config.simmat))
            print(graph_a)
            pert_graph.draw_and_find_cycle(workdir=os.path.join(config.working_path, "ligands"), lig_names=config.ligands, graph_a=graph_a, png_files=png_files)

            with open(os.path.join(config.working_path, "ligands", "graph_doe.pickle"), 'wb') as pfile:
                pickle.dump(config.graph_doe, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump(graph_a, pfile, pickle.HIGHEST_PROTOCOL)
                pickle.dump('tanimoto_fingerprint', pfile, pickle.HIGHEST_PROTOCOL)

            self.graphics_pertGraph.clear_graph()
            self.graphics_pertGraph.init_graph(graph_a=graph_a, names=config.ligands, imgs=png_files)

            # self.get_table(self.tableWidget_cycles, table_path=os.path.join(config.working_path, "ligands", "cycles.csv"),
            #                headers=self.cycles_headers)
            self.get_pair_table(self.tableWidget_pairs, table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            self.get_pair_table(self.tab_mapping.tableWidget, table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            # self.comboBox_update_pairs(self.combo_select_pair)
            # self.comboBox_update_pairs(self.combo_select_pair_anal)

            pert_names = ",\n".join(pert_list)
        except Exception as e:
            # self.logger.error('fail to set job folder')
            print(e)
            pass
        # for line in os.listdir(self.ligands_path):
        #     if ".mol" in line:
        #         self.ligands.append(line.strip())
        # 将当前的ligands 信息输入到ligands file
        print(config.pairs)

    def update_pert_map_setup(self, pert_names):
        pert_map_setup_txt = \
            """mode		= map
            list_pert   = %s
        
            top_sep     = False
            lig1		= ligand.mol
            outdir		= ../perturbations
            reverse		= False
            heavyH      = False"""
        if os.path.exists("pert_map_setup.in"):
            s = open("pert_map_setup.in", 'r+').read()
            pert_map_setup = re.sub(r"list_pert[\s\S]+top_sep", "list_pert   = %s\ntop_sep" % pert_names, s)
        else:
            pert_map_setup = pert_map_setup_txt % (pert_names)
        open("pert_map_setup.in", 'w+').write(pert_map_setup)

    def update_pert_map_regen(self, pert_names):
        pert_map_regen_txt = \
            """mode		= map
            mapfile     = map_given.txt
            list_pert 	= %s
        
            top_sep		= False
            lig1		= ligand.mol
            outdir		= ../perturbations
            reverse		= False
            heavyH      = False"""
        if os.path.exists("pert_map_regen.in"):
            s = open("pert_map_regen.in", 'r+').read()
            pert_map_regen = re.sub(r"list_pert[\s\S]+top_sep", "list_pert   = %s\ntop_sep" % pert_names, s)
        else:
            pert_map_regen = pert_map_regen_txt % (pert_names)
        open("pert_map_regen.in", 'w+').write(pert_map_regen)

    def update_pert_top_setup(self, pert_names):
        pert_top_setup_txt = \
            """mode		= pert
            mapfile     = map_after_dummy.txt
            list_pert 	= %s
        
            top_sep		= False
            lig1		= ligand.mol
            top1		= Lig.top
            outfile		= ffMOL.itp, merged.itp, merged.top, mergedA.pdb, mergedA.gro
            outdir		= ../perturbations
            reverse		= False
            heavyH      = False"""
        if os.path.exists("pert_top_setup.in"):
            s = open("pert_top_setup.in", 'r+').read()
            pert_top_setup = re.sub(r"list_pert[\s\S]+top_sep", "list_pert   = %s\ntop_sep" % pert_names, s)
        else:
            pert_top_setup = pert_top_setup_txt % (pert_names)
        open("pert_top_setup.in", 'w+').write(pert_top_setup)

    # 获取pair表格信息
    def get_pair_table(self, table_widget, table_path=None, headers=None):
        if table_path == None:
            # 在没数据的情况下 确定headers
            if headers != None:
                table_widget.setColumnCount(len(headers))

                for i in range(len(headers)):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(headers[i])

                    if i == len(headers) - 1:
                        root = QFileInfo('ArrowDouble.png').absolutePath()
                        icon = QIcon(root + '/fep_modules/imgs/ArrowDouble.png')
                        item.setIcon(icon)
                    table_widget.setHorizontalHeaderItem(i, item)
            return 0
        if not os.path.exists(table_path):
            return 0
        data = open(table_path).read().strip().split("\n")
        if not headers:
            headers = data[0].split(',')
        row = len(data) - 1
        column = len(headers)
        table_widget.setColumnCount(column)
        table_widget.setRowCount(row)
        # 确定表头
        for i in range(column):

            item = QtWidgets.QTableWidgetItem()
            item.setText(headers[i])
            if i == column - 1:
                root = QFileInfo('ArrowDouble.png').absolutePath()
                icon = QIcon(root + '/fep_modules/imgs/ArrowDouble.png')
                item.setIcon(icon)



            table_widget.setHorizontalHeaderItem(i, item)
        # 确定行index
        for i in range(row):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i))
            table_widget.setVerticalHeaderItem(i, item)

        table_widget.horizontalHeader().sectionClicked.connect(lambda index: my_util.sort_table(index, table_widget))
        # 确定数据内容
        data = data[1:]
        for i in range(row):
            tmp_data = re.split('[,~]', data[i])
            # tmp_data = data[i].split(',')
            for j in range(column):
                item = QtWidgets.QTableWidgetItem()
                item.setText(tmp_data[j])
                table_widget.setItem(i, j, item)
        __sortingEnabled = table_widget.isSortingEnabled()
        table_widget.setSortingEnabled(False)
        table_widget.setSortingEnabled(__sortingEnabled)
        # table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # table_widget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

    # 获取ligand表格信息
    def get_ligand_table(self, table_path=None):
        headers = ['Name', 'Crystal\nStructure', 'Exp. Affinity (kcal/mol)', 'Exp. Error (kcal/mol)',
                                'Weight']
        if table_path == None:
            # 在没数据的情况下 确定headers
            # if headers != None:
            #     table_widget.setColumnCount(len(headers))
            #
            #     for i in range(len(headers)):
            #         item = QtWidgets.QTableWidgetItem()
            #         item.setText(headers[i])
            #
            #         if i == len(headers) - 1:
            #             root = QFileInfo('ArrowDouble.png').absolutePath()
            #             icon = QIcon(root + '/fep_modules/imgs/ArrowDouble.png')
            #             item.setIcon(icon)
            #         table_widget.setHorizontalHeaderItem(i, item)
            return 0
        if not os.path.exists(table_path):
            return 0
        data = open(table_path).read().strip().split("\n")
        # if not headers:
        #     headers = data[0].split(',')
        row = len(data) - 1
        # column = len(headers)
        # self.tableWidget_ligands.setColumnCount(column)
        print(self.tableWidget_ligands.columnCount())
        column = self.tableWidget_ligands.columnCount()
        self.tableWidget_ligands.setRowCount(row)

        # 确定数据内容
        data = data[1:]
        for i in range(row):
            tmp_data = data[i].split(',')
            for j in range(column):
                item = QtWidgets.QTableWidgetItem()
                item.setText(tmp_data[j])
                self.tableWidget_ligands.setItem(i, j, item)
        # __sortingEnabled = self.tableWidget_ligands.isSortingEnabled()
        # self.tableWidget_ligands.setSortingEnabled(False)
        # self.tableWidget_ligands.setSortingEnabled(__sortingEnabled)

    def sort_table(self, table_widget):
        if table_widget.currentColumn() == 2:
            if self.table_descending:
                table_widget.sortItems(2, Qt.AscendingOrder)
                self.table_descending = False
            else:
                table_widget.sortItems(2, Qt.DescendingOrder)
                self.table_descending = True

    # 进行generate 操作
    def generate(self):
        try:
            param = json.loads(open(os.path.join(config.working_path, "param", "ligands.json")).read())
            job_dir = config.working_path
            similarity_method = param["similarity_method"]
            optimal_criteria = param["optimal_criteria"]
            number_of_cycles = param["number_of_cycles"]
            init = 'MST'
            parallel = False
            lig_names, graph_a, png_files = pert_graph.pert_graph(job_dir=job_dir, lignames=None,
                                                                  has_exp_data=config.has_exp_data,
                                                                  similarity_method=similarity_method,
                                                                  optimal_criteria=optimal_criteria,
                                                                  number_of_cycles=number_of_cycles, init=init,
                                                                  parallel=parallel)
            # pic_path = os.path.join(self.working_path, "ligands", "perturbation_graph.png")
            # self.get_pic(self.graphics_pertGraph, pic_path=pic_path, keepRatio=True)

            self.graphics_pertGraph.clear_graph()
            self.graphics_pertGraph.init_graph(graph_a=graph_a, names=lig_names, imgs=png_files)

            # self.get_table(self.tableWidget_cycles,
            #                table_path=os.path.join(config.working_path, "ligands", "cycles.csv"),
            #                headers=self.cycles_headers)
            self.get_pair_table(self.tableWidget_pairs,
                           table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            self.get_pair_table(self.tab_mapping.tableWidget,
                           table_path=os.path.join(config.working_path, "ligands", "pairs.csv"),
                           headers=config.pairs_headers)
            # self.comboBox_update_pairs(self.combo_select_pair)
            # self.comboBox_update_pairs(self.combo_select_pair_anal)
            os.chdir(os.path.join(job_dir, "ligands"))
            pert_top.FEprep("pert_map_setup.in")
            QMessageBox.information(QWidget(), 'Success', 'Success generate ')
        except Exception as e:
            QMessageBox.critical(QWidget(), 'Error', str(e))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_mapping = MyPerturbation()
    my_mapping.show()
    sys.exit(app.exec_())
