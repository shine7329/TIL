# 다익스트라 

import heapq
def dijkstra(graph, start):
    distance = [float("inf")] * (V + 1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        node = heapq.heappop(queue)
        if distance[node[1]] < node[0]:
            continue
        for next_node in graph[node[1]]:
            cost = node[0] + next_node[0]
            if distance[next_node[1]] > cost:
                distance[next_node[1]] = cost
                heapq.heappush(queue, (cost, next_node[1]))