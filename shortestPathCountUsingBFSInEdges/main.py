# Given the below edges find the shortest path count between src and dest nodes

import queue

q = queue.Queue()
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],
    ['y', 'a'],
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd']
]


def get_graph(edges):
    graph = {}
    for node_a, node_b in edges:
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    return graph


def find_shortest_path_between_src_and_dest(graph, src, dest, visited):
    q.put((src, 0))
    while not q.empty():
        current, current_count = q.get()
        # print(f"{current} {current_count}")
        if current == dest:
            return current_count
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_count = current_count + 1
                q.put((neighbor, new_count))
    return 0


graph = get_graph(edges)
# print(f'{graph}')
# print(find_shortest_path_between_src_and_dest(graph, 'w', 'z', set())) #Answer: 2
# print(find_shortest_path_between_src_and_dest(graph, 'w', 'b', set())) #Answer: 4
print(find_shortest_path_between_src_and_dest(graph, 'w', 't', set())) #Answer: 0 (path doesnt exists)
# print(find_shortest_path_between_src_and_dest(graph, 'w', 'y', set())) #Answer: 2
# print(find_shortest_path_between_src_and_dest(graph, 'w', 'v', set())) #Answer: 1
# print(find_shortest_path_between_src_and_dest(graph, 'w', 'd', set()))   #Answer: 6
