from graph_interface import *
from graph_data import graph

def dijkstra(graph: nx.Graph, start: str) -> dict:
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, node in graph[current_vertex].items():
            distance = distances[current_vertex] + node['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

def show_shortest_path_way(graph: nx.Graph) -> None:
    all_pairs_shortest_paths = {node: dijkstra(graph, node) for node in graph.nodes()}
    for node, neighbors in all_pairs_shortest_paths.items():
        print(f"Найкоротші шляхи від {node}:")
        for neighbor, weight in neighbors.items():
            print(f"До {neighbor}: {weight}")
        print('_' * 64 + '\n')


def task3() -> None:
    new_graph = create_graph(graph, is_loaded=True)
    show_graph(new_graph)
    show_shortest_path_way(new_graph)
    print(sorted(dijkstra(new_graph, 'A').items(),  key=lambda item: item[1]))
    
    shortest_path_lengths = nx.single_source_dijkstra_path_length(new_graph, source='A')
    print('\n\nПеревірка правильності розрахунку розробленого та бібліотечного алгоритмів Дейкстри \n')
    
    print('Розроблений алгоритм Дейкстри:')
    print(sorted(dijkstra(new_graph, 'A').items(),  key=lambda item: item[1]))
    
    print('Бібліотечний алгоритм Дейкстри:')
    print(shortest_path_lengths) 


if __name__ == "__main__":
    task3()