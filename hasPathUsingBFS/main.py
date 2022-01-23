# Write a function hasPat that takes in an object representing the adjacency list of a directed acyclic graph and two
# nodes(src, dest)The function should return a boolean indicating whethere or not there exists a directed path between the soure and destination nodes

# This solution is using BFS algorithm
# Solution: BFS makes use of a queue which is LIFO
# Time complexity is  O(|number of nodes| + |number of edges|)
# Space complexity is O(|number of nodes|)

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
def has_path(graph, src, dest):
    q.put(src)
    while not q.empty():
        current = q.get()
        if current == dest:
            return True
        for neighbor in graph[current]:
            q.put(neighbor)
    return False


print(has_path(graph, 'f', 'j'))
# src=f, dest=k, return True
# src=f, dest=j, return False




