import queue

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

q = queue.Queue()


def traverse_using_BFS_without_tracking_visited(graph, src):
    q.put(src)
    while not q.empty():
        current = q.get()
        print(f'{current}')
        for neighbor in graph[current]:
            q.put(neighbor)
    return


def traverse_using_BFS_tracking_visited(graph, src, visited):
    q.put(src)
    while not q.empty():
        current = q.get()
        visited.add(current)
        print(f'{current}')
        for neighbor in graph[current]:
            if neighbor not in visited:
                q.put(neighbor)
    return

# print('Without tracking visited:')
# traverse_using_BFS_without_tracking_visited(graph, 'f')  # should print f, g, i, h, g, k, h
# traverse_using_BFS_without_tracking_visited(graph, 'j')  # should print j, i, g, k , h

print('Tracking visited:')
# traverse_using_BFS_tracking_visited(graph, 'f', set())  # should print f, g, i, h, k
traverse_using_BFS_tracking_visited(graph, 'j', set())  # should print j, i, g, k , h