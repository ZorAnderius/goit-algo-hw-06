import networkx as nx
import matplotlib.pyplot as plt

from typing import Callable

from graph_interface import create_graph, show_graph
from graph_data import graph

def analyze_graph(graph: nx.Graph, func: Callable) -> None:
    try:
        counter = 0
        str = '' 
        for k, v in func(graph).items():
            str += f'{k} : {v:.3f}    '
            counter += 1
            if counter == 4:
                print(str)
                str = ''
                counter = 0
                    
        if str:
            print(str)
    except Exception:
        print('Функція не знайдена')

def vertex_analyze(graph: nx.Graph) -> None:
    try:
        counter = 0
        str = ''
        for k, v in graph.degree():
            str += f'{k} : {v}    '
            counter += 1
            if counter == 4:
                print(str)
                str = ''
                counter = 0
            
        if str:
            print(str)
    except Exception:
        print('Функція не знайдена')

def task1() -> None:
    G = create_graph(graph)
    show_graph(G)
    print('Аналіз графа:')
    print('_' * 64 + '\n')
    print('Кількість вершин:  ', G.number_of_nodes())
    print('Кількість ребер:  ', G.number_of_edges())
    print('_' * 64 + '\n')
    print('Граф є звязним? ', 'Так' if nx.is_connected(G) else 'Ні')
    print('_' * 64 + '\n')
    print('Густина графа: ', f'{nx.density(G):.4f}')
    print('_' * 64 + '\n')
    print('Cтупені вершин: ')
    vertex_analyze(G)
    print('_' * 64 + '\n')
    print('Ступінь центральності (кількість ребер для вузла):')
    analyze_graph(G, nx.degree_centrality)
    print('_' * 64 + '\n')
    print('Близькість вузла до інших вузлів: ')
    analyze_graph(G, nx.closeness_centrality)
    print('_' * 64 + '\n')
    print('''Посередництво вузла (кількість найкоротших шляхів між усіма 
парами вузлів, які проходять через даний вузол):''')
    analyze_graph(G, nx.betweenness_centrality)


if __name__ == "__main__":
    task1()