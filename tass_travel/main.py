from tools.analyzer import Analyzer
from tools.graph_builder import GraphBuilder


def main():
    graph = GraphBuilder('2005-01-01', '2008-01-01').build()
    print("Number of nodes:", graph.number_of_nodes())
    print(list(graph.nodes.items())[0])
    print("Number of edges:", graph.number_of_edges())
    print(list(graph.edges.items())[0])

    popular_cities = Analyzer.get_popular_cities(graph)
    best_poi = Analyzer.get_best_poi_cities(popular_cities, ['tourism'], [])

    print("\nPopular cities:")
    for c in best_poi:
        print(c)


if __name__ == '__main__':
    main()
