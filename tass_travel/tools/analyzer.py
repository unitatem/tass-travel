from tass_travel.tools.database import Database


class Analyzer:
    @staticmethod
    def get_popular_cities(graph):
        sorted_weights = sorted(graph.degree(weight='weight'), reverse=True)
        sorted_degrees = sorted(graph.degree,  reverse=True)

        # filter nodes which have degree > 0
        sorted_degrees = [(n, v) for n, v in sorted_degrees if v > 0]
        # filter nodes which have weights > 0
        sorted_weights = [(n, v) for n, v in sorted_weights if v > 0]

        zipped = list(map(
            lambda item: (item[0][0], (item[0][1])/(item[1][1])),
            zip(sorted_weights, sorted_degrees)
        ))

        sorted_normalized = sorted(zipped, key=lambda x: x[1], reverse=True)

        popular_cities = []
        for k, d in sorted_normalized:
            node = graph.nodes[k]
            node['id'] = k
            popular_cities.append(node)
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
        best_poi = best_poi[:30]
        return best_poi
