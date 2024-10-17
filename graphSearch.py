# dij - given a graph, find the shortest distance from a source node to all other nodes, return ret[n] - O((V+E)log V) - pq length is V+E, each time updating takes logV
# floyed - given a graph, find the shortest distance between all pairs, return ret[n][n] - O(n^3)
# edges: [(source, dest, dist)]
import heapq


# dijsktra find the min distance from 1 node to all other nodes
# use a priority queue to save ([distance, node]), return the node when min distance until pq is exhausted
#  initialize dist[] with dist[source] = 0 and dist[others] = float('inf')
#  initially pq only has ([0, source])
#  while pq is not empty, pop one from pq, for all source's neighbour,
#   compare dist[dest] and dist[source] + edge(source, neighbour)
#   if later is smaller, found a shorter path
#       update dist[dest] = newDest
#       heap push [newDest, dest] to the queue

# note:
#  initialize dist[] with dist[source] = 0
#  initialize pq with only one node

def dij(source, edges):
    nodes = set()
    # {source: {dest: dist}}
    neighbours = {}
    for s, d, dist in edges:
        nodes.add(s)
        nodes.add(d)
        if s not in neighbours:
            neighbours[s] = {}
        neighbours[s][d] = dist

        if d not in neighbours:
            neighbours[d] = {}
        neighbours[d][s] = dist

    dist = [float('inf')] * len(nodes)
    dist[source] = 0

    pq = [[0, source]]

    heapq.heapify(pq)

    while pq:
        minDistance, sourceNode = heapq.heappop(pq)
        if minDistance > dist[sourceNode]:
            continue
        for dest in neighbours[sourceNode]:
            d = neighbours[sourceNode][dest]
            if dist[sourceNode] + d < dist[dest]:
                print("  process the node")
                dist[dest] = dist[sourceNode] + d
                # directly push it, no need to update, as the bad node won't update the distance and will get skipped
                heapq.heappush(pq, [dist[dest], dest])

    print(dist)


# find shortest path between all paris, return a dist[n][n]
def floyedWarshall(edges):
    nodes = set()
    # {src: {dst: dist}}
    neighbours = {}
    for src, dst, dist in edges:
        nodes.add(src)
        nodes.add(dst)
        if src not in neighbours:
            neighbours[src] = {}
        neighbours[src][dst] = dist

        if dst not in neighbours:
            neighbours[dst] = {}
        neighbours[dst][src] = dist

    n = len(nodes)
    ret = [[float('inf')] * n for _ in range(n)]

    # initialize 1: self to self is 0
    for i in range(n):
        ret[i][i] = 0
    # initialize 2: initial distance is edge length
    for src, dst, dist in edges:
        ret[src][dst] = dist
        ret[dst][src] = dist

    for fromNode in range(n):
        for toNode in range(n):
            for throughNode in range(n):
                ret[fromNode][toNode] = min(ret[fromNode][toNode], ret[fromNode][throughNode] + ret[throughNode][toNode])
                # no neeed for this, as later toNode and fromNode will also be run
                # ret[toNode][fromNode] = ret[fromNode][toNode]

    for row in ret:
        print(row)




if __name__ == '__main__':
    # dij(0, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]])
    floyedWarshall([[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]])
