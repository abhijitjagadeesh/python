# Write a function hasPat that takes in an object representing the adjacency list of a directed acyclic graph and two
# nodes(src, dest)The function should return a boolean indicating whethere or not there exists a directed path between the soure and destination nodes

# This solution is using DFS algorithm
# Solution: DFS makes use of stack in recursive calls which is FIFO
# Time complexity is  O(|number of nodes| + |number of edges|)
# Space complexity is O(|number of nodes|)

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path(graph, src, dest):
    if src == dest:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest):
            return True
    return False


print(has_path(graph, 'f', 'j'))
# src=f, dest=k, return True
# src=f, dest=j, return False




