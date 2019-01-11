from database import Database


class Analyzer:
    @staticmethod
    def get_popular_cities(graph):
        # TODO popular average destinations, this is mock, use some graph property
        popular_cities = []
        for k, v in graph.nodes.items():
            if k > 30:
                continue
            v['id'] = k
            popular_cities.append(v)
        return popular_cities

    @staticmethod
    def get_best_poi_cities(cities, types, values):
        db = Database()
        db.open_transaction()

        best_poi = []
        for c in cities:
            c['normalized_poi'] = db.count_poi(c['id'], type=types) / c['population']
            best_poi.append(c)

        db.close_transaction()

        best_poi = sorted(best_poi, key=lambda x: x['normalized_poi'], reverse=True)
        return best_poi
