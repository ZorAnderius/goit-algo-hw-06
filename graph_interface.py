import networkx as nx
import matplotlib.pyplot as plt
from random import randint


def create_graph(graph: dict, is_loaded: bool=False) -> nx.Graph:
    G = nx.Graph(graph)
    if is_loaded:
        for (u, v) in G.edges():
            G[u][v]['weight'] = randint(1,10) *10
    return G

def show_graph(graph : nx.Graph) -> None:
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw_networkx(graph, pos, with_labels=True, node_size=900, node_color="lightblue", font_size=16, font_weight="bold")
    
    if is_loaded_graph(graph):
        edge_labels = {(i, j): graph[i][j]['weight'] for i, j in graph.edges()}
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()

def is_loaded_graph(graph: nx.Graph) -> bool:
    try:
        for (u, v) in graph.edges():
            if graph[u][v]['weight']:
                return True
    except KeyError:
        return False