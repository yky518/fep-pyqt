import os
import re
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem

from FEprep import pert_top, pert_graph
from fep_modules.config import config
from fep_modules.mapping import Ui_Mapping
from fep_modules.util import my_util


class MyMapping(QtWidgets.QWidget, Ui_Mapping):
    def __init__(self, tabWidget):
        super(MyMapping, self).__init__()
        self.setupUi(self)
        self.Hermite_viewer = None
        self.tabWidget = tabWidget

        self.picfile = ''

        self.currentPair = ''

        self.button_mapRegen.clicked.connect(lambda x: self.regenerate_map())
        # self.tableWidget = MyTable()
        self.tableWidget.table_descending = True
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.itemClicked.connect(lambda: (self.row_select(),
            self.get_pic(self.graphicsView, os.path.join(config.working_path, "perturbations", self.picfile, "images",
                         "aligned.png"))))

        self.button_showMapHermite.clicked.connect(lambda x: (
            self.show_map_in_Hermite()))

        self.button_showPertHermite.clicked.connect(lambda x: (
            self.show_pert_in_Hermite()))
        self.button_browse_map.clicked.connect(lambda x: my_util.read_from_file_click(self.lineEdit_editMapp, basename=True))
        self.button_next_pertGraph.clicked.connect(lambda x: self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1))

    def sort_table(self, table_widget):
        if table_widget.currentColumn() == 2:
            if self.table_descending:
                table_widget.sortItems(2, Qt.AscendingOrder)
                self.table_descending = False
            else:
                table_widget.sortItems(2, Qt.DescendingOrder)
                self.table_descending = True

    def row_select(self):
        self.picfile = self.tableWidget.item(self.tableWidget.currentRow(), 0).text() + '~' + self.tableWidget.item(self.tableWidget.currentRow(), 1).text()

    def show_map_in_Hermite(self):
        if self.Hermite_viewer is not None:
            pair = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            name1, name2 = pair.split('~')
            molfile1 = os.path.join(config.working_path, "ligands", name1, "ligand.mol")
            molfile2 = os.path.join(config.working_path, "ligands", name2, "ligand.mol")
            mapfile = os.path.join(config.working_path, "perturbations", pair, "map_before_dummy.txt")

            self.Hermite_viewer.map_two_mols(molfile1, molfile2, mapfile)
            self.Hermite_mapping_state = 1

    def show_pert_in_Hermite(self):
        if self.Hermite_viewer is not None:
            pair = self.self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            molfile1 = os.path.join(config.working_path, "perturbations", pair, "mergedA.mol")
            molfile2 = os.path.join(config.working_path, "perturbations", pair, "mergedB.mol")
            mapfile = os.path.join(config.working_path, "perturbations", pair, "map_after_dummy.txt")

            self.Hermite_viewer.map_two_mols(molfile1, molfile2, mapfile)
            self.Hermite_mapping_state = 2

    def regenerate_map(self):
        job_dir = config.working_path
        # regen_all = self.check_mapRegen.isChecked()
        # pert_list = [config.pairs[i][0] + "~" + config.pairs[i][1] for i in range(len(config.pairs))]
        # pert_names = ",\n".join(pert_list) if regen_all else self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        pert_names = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        mapfile = self.lineEdit_editMapp.text()
        os.chdir(os.path.join(job_dir, "ligands"))

        if os.path.exists("pert_map_regen.in"):
            s = open("pert_map_regen.in", 'r+').read()
            pert_map_regen = re.sub(r"list_pert[\s\S]+top_sep", "list_pert   = %s\ntop_sep" % pert_names, s)
            pert_map_regen = re.sub(r"mapfile[\s\S]+list_pert", "mapfile     = %s\nlist_pert" % mapfile,
                                    pert_map_regen)
            if mapfile == "":
                pert_map_regen = re.sub(r"mapfile[\s\S]+list_pert", "\nlist_pert", pert_map_regen)
        else:
            pert_map_regen = \
                """mode		= map
                %s
                list_pert 	= %s
            
                top_sep		= False
                lig1		= ligand.mol
                outdir		= ../perturbations
                reverse		= False
                heavyH      = False""" % ("mapfile     = " + mapfile if mapfile != "" else "", pert_names)
        open("pert_map_regen.in", 'w+').write(pert_map_regen)
        pert_top.FEprep("pert_map_regen.in")
        self.get_pic(self.graphics_pertMol,
                     os.path.join(self.working_path, "perturbations", self.picfile,
                                  "images", "aligned.png"))

    def table_select_click(self, row):
        if row != self.currentPair:
            pixmap = QPixmap(os.path.join(self.figpath, str(row) + ".png"))
            self.fig_label.setPixmap(pixmap)

            for i in range(len(self.props)):
                prop = str(self.molprop.loc[row, self.props[i]])
                # self.prop_table.setItem(0, i, QTableWidgetItem(prop))
                self.prop_table.setItem(0, i, QTableWidgetItem(prop))
            self.currentPair = row

    # 获取对应的图片
    def get_pic(self, graphics_view, pic_path=None, keepRatio=False):
        print(pic_path)
        if pic_path == None:
            scene = QGraphicsScene()
            graphics_view.setScene(scene)
            return 0
        if not os.path.exists(pic_path):
            scene = QGraphicsScene()
            graphics_view.setScene(scene)
            return 0
        pix = QtGui.QPixmap()
        pix.load(pic_path)
        if keepRatio:
            pix.width()
            pix = pix.scaled(graphics_view.width(), graphics_view.height(),
                             aspectRatioMode=Qt.KeepAspectRatio,
                             transformMode=Qt.SmoothTransformation)
        else:
            pix.height()
            pix = pix.scaled(graphics_view.width(), graphics_view.height(),
                             aspectRatioMode=Qt.IgnoreAspectRatio,
                             transformMode=Qt.SmoothTransformation)
        # Qt.KeepAspectRatio) Qt::SmoothTransformation Qt.IgnoreAspectRatio
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        graphics_view.setScene(scene)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_mapping = MyMapping()
    my_mapping.show()
    sys.exit(app.exec_())
