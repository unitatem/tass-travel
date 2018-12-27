from graph_builder import GraphBuilder


def main():
    graph = GraphBuilder('2005-01-01', '2008-01-01').build()
    print("Number of nodes:", graph.number_of_nodes())
    print(list(graph.nodes.items())[0])
    print("Number of edges:", graph.number_of_edges())
    print(list(graph.edges.items())[0])

    # TODO popular average destinations, this is mock, use some graph property
    popular_cities = []
    for k, v in graph.nodes.items():
        if k > 30:
            continue
        v['id'] = k
        v['normalized_poi'] = v['poi_cnt'] / v['population']
        popular_cities.append(v)

    popular_cities = sorted(popular_cities, key=lambda x: x['normalized_poi'], reverse=True)
    print("\nPossible popular cities:")
    for c in popular_cities:
        print(c)


if __name__ == '__main__':
    main()
