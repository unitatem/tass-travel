import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from analyzer import Analyzer
from application.gui import Ui_MainWindow
from graph_builder import GraphBuilder


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.filterBtn.clicked.connect(self._filter_btn_clicked)

    def _filter_btn_clicked(self):
        graph = self._build_graph_by_dates()
        popular_cities = Analyzer.get_popular_cities(graph)
        types = self._extract_activity_types()
        best_poi = Analyzer.get_best_poi_cities(popular_cities, types, [])
        self._present_best_cites_by_poi(best_poi)

    def _build_graph_by_dates(self):
        start_date = self.startDate.date().toString("yyyy-MM-dd")
        end_date = self.endDate.date().toString("yyyy-MM-dd")
        print("start_date:", start_date, "end_date:", end_date)

        graph = GraphBuilder(start_date, end_date).build()
        print("number of nodes:", graph.number_of_nodes())
        print("number of edges:", graph.number_of_edges())
        return graph

    def _extract_activity_types(self):
        types = []
        if self.checkBox_1.isChecked():
            types.append('leisure')
        if self.checkBox_2.isChecked():
            types.append('historic')
        if self.checkBox_3.isChecked():
            types.append('tourism')
        return types

    def _present_best_cites_by_poi(self, best_poi):
        print("Popular cities:")
        self.table.setRowCount(0)
        for idx, c in enumerate(best_poi):
            print(c)
            self.table.insertRow(idx)
            self.table.setItem(idx, 0, QtWidgets.QTableWidgetItem(c['name']))
            self.table.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(c['population'])))
            self.table.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(c['normalized_poi'])))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = App()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
