from database import Database
from graph_builder import GraphBuilder


def main():
    graph = GraphBuilder('2005-01-01', '2008-01-01').build()
    print("number of nodes:", graph.number_of_nodes())
    print(graph.nodes[3])
    print("number of edges:", graph.number_of_edges())
    print(graph.edges[3, 4])
    #
    # # TODO popular average destinations
    # popular_cities = {}
    # for k, v in graph.nodes.items():
    #     if k > 30:
    #         break
    #     popular_cities[k] = v
    # print(popular_cities)
    #
    # # find poi cnt in that regions
    # db = Database()
    # db.open_transaction()
    #
    # geo = db.find_city_geo_by_name("Monaco")
    # print(geo)
    #
    # db.close_transaction()

    # present list sorted by


if __name__ == '__main__':
    main()
