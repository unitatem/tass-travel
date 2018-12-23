from graph_builder import GraphBuilder


def main():
    graph = GraphBuilder('2005-01-01', '2008-01-01').build()
    print("number of nodes:", graph.number_of_nodes())
    print(graph.nodes[3])
    print("number of edges:", graph.number_of_edges())
    print(graph.edges[3, 4])


if __name__ == '__main__':
    main()
