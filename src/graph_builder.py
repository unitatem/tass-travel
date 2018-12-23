import networkx as nx

from database import Database


class GraphBuilder:
    def __init__(self, from_date, to_date):
        self._graph = nx.DiGraph()
        self._db = Database()
        self._from_date = from_date
        self._to_date = to_date

    def build(self):
        self._db.open_transaction()
        self._cities()
        self._flights()
        self._db.close_transaction()
        return self._graph

    def _cities(self):
        cities = self._db.get_all_cities()
        for city in cities:
            self._graph.add_node(city['id'], name=city['name'], population=city['population'])

    def _flights(self):
        flights = self._db.get_flights(self._from_date, self._to_date)
        for flight in flights:
            self._graph.add_edge(flight['from'], flight['to'], weight=flight['passengers'])
