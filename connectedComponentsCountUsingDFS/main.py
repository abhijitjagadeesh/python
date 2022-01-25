graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}


def traverse_path(graph, src, visited):
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        traverse_path(graph, neighbor, visited)
    return True

def count_connected_node(graph):
    count = 0
    visited = set()
    for node in graph.keys():
        if traverse_path(graph, node, visited):
            count += 1
    return count


print(count_connected_node(graph)) # Should print 3
