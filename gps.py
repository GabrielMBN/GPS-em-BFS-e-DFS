cities = {
    'Vitória': ( -20.3194, -40.3378 ),
    'Vila Velha': ( -20.3297, -40.2922 ),
    'Cariacica': ( -20.2635, -40.4165 ),
    'Serra': ( -20.1211, -40.3074 ),
    'Guarapari': ( -20.6693, -40.4973 ),
    'Linhares': ( -19.3959, -40.0642 ),
    'Colatina': ( -19.5396, -40.626 ),
    'Aracruz': ( -19.819, -40.2768 ),
    'Cachoeiro de Itapemirim': ( -20.8477, -41.1126 ),
    'Nova Venécia': ( -18.7151, -40.4058 ),
    'São Mateus': ( -18.7213, -39.8576 ),
    'Barra de São Francisco': ( -18.7552, -40.8979 ),
    'Santa Teresa': ( -19.9366, -40.5979 ),
    'Venda Nova do Imigrante': ( -20.3264, -41.1356 ),
    'Santa Maria de Jetibá' : (-20.025669892220293, -40.74327676550917),
    'Santa Leopoldina' : (-20.10056796652768, -40.52775994730116),
}

roads = [
    ('Vitória', 'Vila Velha', 9),
    ('Vitória', 'Santa Teresa', 52),
    ('Vitória', 'Cariacica', 10),
    ('Vila Velha', 'Cariacica', 12),
    ('Vila Velha', 'Guarapari', 60),
    ('Cariacica', 'Serra', 16),
    ('Serra', 'Nova Venécia', 140),
    ('Serra', 'Linhares', 156),
    ('Guarapari', 'Linhares', 157),
    ('Linhares', 'São Mateus', 87),
    ('Linhares', 'Barra de São Francisco', 78),
    ('Linhares', 'Santa Teresa', 82),
    ('São Mateus', 'Nova Venécia', 62),
    ('São Mateus', 'Barra de São Francisco', 95),
    ('São Mateus', 'Santa Teresa', 105),
    ('Barra de São Francisco', 'Nova Venécia', 44),
    ('Santa Teresa', 'Venda Nova do Imigrante', 21),
    ('Santa Teresa', 'Cachoeiro de Itapemirim', 166),
    ('Santa Teresa', 'Santa Leopoldina', 20),
    ('Santa Teresa', 'Santa Maria de Jetibá', 19),
    ('Santa Leopoldina', 'Vila Velha', 36),
    ('Santa Leopoldina', 'Santa Maria de Jetibá', 24),
    ('Cachoeiro de Itapemirim', 'Venda Nova do Imigrante', 118),
    ('Cachoeiro de Itapemirim', 'Aracruz', 167),
    ('Aracruz', 'Nova Venécia', 117),
    ('Aracruz', 'Linhares', 50),
]

from collections import deque

def bfs(cities, roads, start, end):
    queue = deque([start])
    visited = {start: None}
    while queue:
        current_city = queue.popleft()
        if current_city == end:
            path = []
            while current_city:
                path.append(current_city)
                current_city = visited[current_city]
            path.reverse()
            return path
        for neighbor, distance in get_neighbors(current_city, roads):
            if neighbor not in visited:
                visited[neighbor] = current_city
                queue.append(neighbor)

def get_neighbors(city, roads):
    neighbors = []
    for road in roads:
        if city in road:
            neighbor = road[0] if road[1] == city else road[1]
            distance = road[2]
            neighbors.append((neighbor, distance))
    return neighbors

def dfs(cities, roads, start, end):
    stack = [start]
    visited = {start: None}
    while stack:
        current_city = stack.pop()
        if current_city == end:
            path = []
            while current_city:
                path.append(current_city)
                current_city = visited[current_city]
            path.reverse()
            return path
        for neighbor, distance in get_neighbors(current_city, roads):
            if neighbor not in visited:
                visited[neighbor] = current_city
                stack.append(neighbor)

def calculate_distance(path, roads):
    distance = 0
    for i in range(len(path) - 1):
        for road in roads:
            if (path[i] == road[0] and path[i+1] == road[1]) or \
                (path[i] == road[1] and path[i+1] == road[0]):
                distance += road[2]
                break
    return distance


start = input("Informe a cidade de origem: ")
end = input("Informe a cidade de destino: ")
search_type = input("Escolha a busca cega (BFS ou DFS): ")

if search_type.upper() == "BFS":
    path = bfs(cities, roads, start, end)
elif search_type.upper() == "DFS":
    path = dfs(cities, roads, start, end)

if path:
    distance = calculate_distance(path, roads)
    print("\nDistância:", distance, "Km");
    print("Caminho percorrido:", path)
