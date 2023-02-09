def dijkstra(graph, start, end):
    # Create a dictionary to store the distance from the start node to every other node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Create a dictionary to store the previous node for each node
    previous = {}

    # Create a set to keep track of unvisited nodes
    unvisited = set(graph)

    # Create a set to keep track of the current node
    current = start

    while current != end:
        for neighbor in graph[current]:
            new_distance = distances[current] + graph[current][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

        unvisited.remove(current)
        if not unvisited:
            return None, None
        candidates = {node: distances[node] for node in unvisited}
        current = min(candidates, key=candidates.get)

    # Create a list to store the shortest path
    path = []
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return path, distances[end]

# Example usage:
graph = {
    "A": {"B": 7, "C": 3, "D":2, "E":2},
    "B": {"A": 7, "C": 1},
    "C": {"A": 3, "B": 1, "E": 4,"F":3},
    "D": {"A": 2, "E": 1,"G":2,"F":10},
    "E": {"A":2,"C":4,"D":1,"F":4,"G":2},
    "F": {"C":3,"D":10,"E":4,"G":7},
    "G": {"D":2,"E":2,"F":7}
}

shortest_path, shortest_distance = dijkstra(graph, "B", "G")

print("Shortest Path: ", shortest_path)
print("Shortest Distance: ", shortest_distance)
