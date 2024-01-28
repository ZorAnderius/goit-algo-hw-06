from collections import deque

from graph_data import graph

def dfs_recursive(graph: dict, vertex: str, visited: set=None) -> None:
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex) if len(visited) == len(graph) else print(vertex, end=" -> ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_recursive(graph: dict, queue: deque, visited: set=None) -> None:
    if visited is None:
        visited = set()

    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex) if len(visited) == len(graph) - 1 else print(vertex, end=" -> ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

def task2() -> None:
    print('DFS пошук:')
    dfs_recursive(graph, 'A')
    print()
    print('BFS пошук:')
    bfs_recursive(graph, deque(["A"]))


if __name__ == "__main__":
    task2()