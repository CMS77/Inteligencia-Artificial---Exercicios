import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time
import tracemalloc  # Import the tracemalloc module

def ucs_with_state_verification(graph, start, target):
    pq = [(0, start, [])]
    visited = set()

    start_time = time.time()  # Record the start time
    tracemalloc.start()  # Start tracing memory allocations

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            path = path + [node]

            if node == target:
                end_time = time.time()  # Record the end time
                print("\nFim. Nó 18 aberto.")
                print("Tempo de execução:", end_time - start_time, "segundos")
                current, peak = tracemalloc.get_traced_memory()
                print("Memória(bytes):", peak)
                tracemalloc.stop()  # Stop tracing memory allocations
                return path  # Return the path if the target node is reached

            for neighbor, attrs in graph[node].items():
                neighbor_cost = attrs['weight']
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + neighbor_cost, neighbor, path))
    return None

# Create a directed graph with 19 nodes and edges
G = nx.DiGraph()

edges = [(0, 1, {'weight': 5}), (0, 2, {'weight': 3}), (1, 3, {'weight': 4}), (1, 4, {'weight': 2}),
         (2, 5, {'weight': 1}), (2, 6, {'weight': 3}), (3, 7, {'weight': 2}), (3, 8, {'weight': 3}),
         (4, 9, {'weight': 4}), (4, 10, {'weight': 2}), (5, 11, {'weight': 1}), (5, 12, {'weight': 3}),
         (6, 13, {'weight': 2}), (6, 14, {'weight': 1}),(7, 12, {'weight': 1}), (7, 15, {'weight': 2}), (7, 16, {'weight': 3}),
         (8, 17, {'weight': 2}), (8, 18, {'weight': 2}), (12, 7, {'weight': 1}), (14, 12, {'weight': 1}), (16, 18, {'weight': 1}), (17, 7, {'weight': 1})]

G.add_edges_from(edges)

pos = {0: (4.2, 0.8), 1: (2.8, 0.6), 2: (6, 0.9), 3: (3.3, 0.36), 4: (1, 0.65), 5: (5.8, 0.67),
       6: (7.7, 0.7), 7: (5.5, 0.25), 8: (2.3, 0.19), 9: (2, 0.8), 10: (1.4, 0.4), 11: (4, 0.62),
       12: (5.2, 0.42), 13: (9, 0.5), 14: (7, 0.48), 15: (7.4, 0.25), 16: (5.2, 0.030),
       17: (4.1, 0.2), 18: (3.2, 0.020)}

# Perform UCS to find the solution path
target_node = 18
visited_with_state_check = set()
print("Custo Uniforme:")
path = ucs_with_state_verification(G, start=0, target=target_node)
print("Caminho escolhido:", path)

# Visualize the graph and solution path
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', arrows=True)

# Draw the solution path in red
caminho = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=caminho, edge_color='red', width=2)

plt.title("Graph with UCS Solution Path (0 to 18)")
plt.axis('off')
plt.show()
