import networkx as nx
import matplotlib.pyplot as plt
import time
import tracemalloc  # Import the tracemalloc module

# Define a modified BFS function to find a path from 'start' to 'target'
def bfs_cverificacao(graph, start, target):
    visited = set()
    queue = [(start, [start])]  # Initialize the queue with the starting node and its path
    visited.add(start)

    start_time = time.time()  # Record the start time
    tracemalloc.start()  # Start tracing memory allocations

    while queue:
        node, path = queue.pop(0)
        print(node, end=" ")  # Print the current node during BFS traversal

        if node == target:
            end_time = time.time()  # Record the end time
            print("\nFim. Nó 18 aberto.")
            print("Tempo de execução:", end_time - start_time, "segundos")
            current, peak = tracemalloc.get_traced_memory()
            print("Memória(bytes):", peak)
            tracemalloc.stop()  # Stop tracing memory allocations
            return path  # Return the path when the target is reached

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  # Add neighbor and its extended path to the queue
# Create a directed graph
G = nx.DiGraph()

# Define the edges of the graph
arestas = [(0, 1), (0, 2), (1, 4), (1, 3), (2, 5), (2, 6), (4, 9), (4, 10), (3, 8), (3, 7), (5, 11), (5, 12), (6, 14), (6, 13), (8, 18), (8, 17), (7, 16), (7, 15),
           (7, 12), (12, 7), (14, 12), (16, 18), (17, 7)]

# Add the edges to the graph
G.add_edges_from(arestas)

# Define positions for nodes in the graph
pos = {0: (4.2, 0.8), 1: (2.8, 0.6), 2: (6, 0.9), 3: (3.3, 0.36), 4: (1, 0.65), 5: (5.8, 0.67), 6: (7.7, 0.7), 7: (5.5, 0.25), 8: (2.3, 0.19), 9: (2, 0.8),
       10: (1.4, 0.4), 11: (4, 0.62), 12: (5.2, 0.42), 13: (9, 0.5), 14: (7, 0.48), 15: (7.4, 0.25), 16: (5.2, 0.030), 17: (4.1, 0.2), 18: (3.2, 0.020)}

# Define the target node
no_final = 18

# Perform BFS and store the path from 0 to 18
print("Busca em Largura:")
path = bfs_cverificacao(G, start=0, target=no_final)
print("Caminho escolhido:", path)

# Draw the graph with node labels and attributes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', arrows=True)

# Extract the edges in the path
caminho = [(path[i], path[i+1]) for i in range(len(path)-1)]

# Draw the edges in the path with a red color
nx.draw_networkx_edges(G, pos, edgelist=caminho, edge_color='red', width=2)

# Set the title and hide axis
plt.title("Grafo com Caminho de 0 para 18")
plt.axis('off')

# Show the graph
plt.show()
