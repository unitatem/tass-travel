import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from application.gui import Ui_MainWindow
from tools.analyzer import Analyzer
from tools.database import Database
from tools.graph_builder import GraphBuilder
from tools.osm_api import OSMQuery


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self._ALL = 'All'
        self._cached_poi_values = self._get_possible_poi_values()
        self._selected_group_name = None

        # table fits whole app width
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.radioButton_1.toggled.connect(lambda: self._exclusive_radio_btn(self.radioButton_1))
        self.radioButton_2.toggled.connect(lambda: self._exclusive_radio_btn(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self._exclusive_radio_btn(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda: self._exclusive_radio_btn(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda: self._exclusive_radio_btn(self.radioButton_5))

        self.filterBtn.clicked.connect(self._filter_btn_clicked)

    def _get_possible_poi_values(self):
        db = Database()
        db.open_transaction()
        result = {}
        for tag in OSMQuery.tag_keys_types:
            r = db.get_poi_values(tag)
            r = [self._ALL] + r
            result[tag] = r
        db.close_transaction()
        return result

    def _exclusive_radio_btn(self, active_btn):
        if not active_btn.isChecked():
            return
        self._selected_group_name = active_btn.text()
        self.dropDown.clear()
        self.dropDown.addItems(self._cached_poi_values[self._selected_group_name])

    def _filter_btn_clicked(self):
        graph = self._build_graph_by_dates()
        popular_cities = Analyzer.get_popular_cities(graph)
        group_name = self._get_activity_type()
        value_name = None
        if group_name is not None:
            v = self._get_value_type()
            if v != self._ALL:
                value_name = v

        best_poi = Analyzer.get_best_poi_cities(popular_cities, group_name, value_name)
        self._present_best_cites_by_poi(best_poi)

    def _build_graph_by_dates(self):
        start_date = self.startDate.date().toString("yyyy-MM-dd")
        end_date = self.endDate.date().toString("yyyy-MM-dd")
        print("start_date:", start_date)
        print("end_date:", end_date)

        graph = GraphBuilder(start_date, end_date).build()
        print("number of nodes:", graph.number_of_nodes())
        print("number of edges:", graph.number_of_edges())
        return graph

    def _get_activity_type(self):
        return self._selected_group_name

    def _get_value_type(self):
        return self.dropDown.currentText()

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
