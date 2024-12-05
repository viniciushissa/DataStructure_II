graph = {
    'A': {'B': 6, 'C': 3},
    'B': {'A': 6, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 3, 'E': 4},
    'D': {'B': 5, 'C': 3, 'E': 2, 'F': 3},
    'E': {'C': 4, 'D': 2, 'F': 5},
    'F': {'D': 3, 'E': 5}
}

def dijkstra(graph, start, end):
    unvisited = list(graph.keys())
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}

    while unvisited:
        current_vertex = None
        current_min_distance = float('infinity')
        for vertex in unvisited:
            if distances[vertex] < current_min_distance:
                current_vertex = vertex
                current_min_distance = distances[vertex]

        if current_vertex is None or current_vertex == end:
            break

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_vertices[neighbor] = current_vertex
                
        unvisited.remove(current_vertex)

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_vertices[current]

    return distances[end], path


start_vertex = 'A'
end_vertex = 'F'
shortest_distance, shortest_path = dijkstra(graph, start_vertex, end_vertex)

print(f"Menor distância de {start_vertex} para {end_vertex}: {shortest_distance}")
print(f"Caminho: {' -> '.join(shortest_path)}")