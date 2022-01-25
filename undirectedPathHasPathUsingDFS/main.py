# write a function undirectedpath that takes in an array of edges for an undirected graph and two nodes (src and dest).
# The function should return a boolean indicating whether or not there exists a path between src and dest


# The edge convereted to graph looks like below:
# {
# 'i': ['j', 'k'],
# 'j': ['i'],
# 'k': ['i', 'm', 'l'],
# 'm': ['k'],
# 'l': ['k'],
# 'o': ['n'],
# 'n': ['o']
# }


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]


def get_graph(edges, src, dest):
    graph = {}
    for node_a, node_b in edges:
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    return graph


def has_path(graph, src, dest, visited):
    if src == dest:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest, visited) == True:
            return True
    return False


def undirected_path(edges, src, dest):
    graph = get_graph(edges, src, dest)
    return has_path(graph, src, dest, set())


# print(undirected_path(edges, 'j', 'm'))  # should return True
# print(undirected_path(edges, 'j', 'o'))  # should return False
print(undirected_path(edges, 'i', 'k'))  # should return True
