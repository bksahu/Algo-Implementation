"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of 
its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before 
V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Example 2:
Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Example 3:
Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0
 
There are other valid topological ordering of the graph too.
"""

from collections import defaultdict, deque

# def topological_sort(vertices, edges):
#     graph = defaultdict(list)
#     for u, v in edges:
#         graph[u] += v,

#     visited = [False]*vertices
#     stack = []

#     def dfs(i):
#         nonlocal stack
#         nonlocal visited
#         visited[i] = True

#         for n in graph[i]:
#             if not visited[i]:
#                 dfs(n)

#         stack += i,

#     for i in range(vertices):
#         if not visited[i]:
#             dfs(i)

#     return stack[::-1]

def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    for u, v in edges:
        graph[u] += v,
        inDegree[v] += 1

    sources = deque([node for node, degree in inDegree.items() if degree == 0])

    while sources:
        currNode = sources.popleft()
        sortedOrder += currNode,
        for child in graph[currNode]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological order not possible if cycle in graph
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

if __name__ == "__main__":
    print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    print(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    print(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))