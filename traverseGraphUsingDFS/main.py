graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def traverse_using_DFS_without_tracking_visited(graph, src):
    print(f'{src}')
    for neighbor in graph[src]:
        traverse_using_DFS_without_tracking_visited(graph, neighbor)
    return


def traverse_using_DFS_tracking_visited(graph, src, visited):
    if src in visited:
        return
    visited.add(src)
    print(f'{src}')
    for neighbor in graph[src]:
        traverse_using_DFS_tracking_visited(graph, neighbor, visited)
    return

# print('Without tracking visited:')
# traverse_using_DFS_without_tracking_visited(graph, 'f') #should print f, g, h, i, g, h, k Beacuse there are no cycles in the graph and we not not tracking visited nodes
# traverse_using_DFS_without_tracking_visited(graph, 'j')  # should print j, i, g, h , k

print('Tracking visited:')
# traverse_using_DFS_tracking_visited(graph, 'f', set()) #should print f, g, h, i, k different from above because we are tracking visited nodes here
traverse_using_DFS_tracking_visited(graph, 'j', set())  # should print j, i, g, h , k