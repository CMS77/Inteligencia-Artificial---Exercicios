import networkx as nx
import matplotlib.pyplot as plt
import time
import tracemalloc  # Import the tracemalloc module

# Define a depth-first search function with path tracking
def dfs_sverificacao(graph, node, target, path):
    print(node, end=" ")
    path.append(node)

    start_time = time.time()  # Record the start time
    tracemalloc.start()  # Start tracing memory allocations
    
    if node == target:
        end_time = time.time()  # Record the end time
        print("\nFim. Nó 18 aberto.")  # Print a message when the target node is found
        print("Tempo de execução:", end_time - start_time, "segundos")
        current, peak = tracemalloc.get_traced_memory()
        print("Memória(bytes):", peak)
        tracemalloc.stop()  # Stop tracing memory allocations
        return path  # Return the path when the target node is found
    
    for neighbor in graph.neighbors(node):
        result = dfs_sverificacao(graph, neighbor, target, path)
        if result is not None:
            return result  # Return the path if the target node is found in the subtree
    path.pop()  # Remove the current node from the path if it doesn't lead to the target
    return None

# Create a directed graph with 18 nodes and edges
G = nx.DiGraph()

# Define the edges of the graph
arestas = [(0, 1), (0, 2), (1, 4), (1, 3), (2, 5), (2, 6), (4, 9), (4, 10), (3, 8), (3, 7), (5, 11), (5, 12), (6, 14), (6, 13), (8, 18), (8, 17), (7, 16), (7, 15),
           (7, 12), (12, 7), (14, 12), (16, 18), (17, 7)]

# Add the edges to the graph
G.add_edges_from(arestas)

# Define positions for nodes in the graph
pos = {0: (4.2, 0.8), 1: (2.8, 0.6), 2: (6, 0.9), 3: (3.3, 0.36), 4: (1, 0.65), 5: (5.8, 0.67), 6: (7.7, 0.7), 7: (5.5, 0.25), 8: (2.3, 0.19), 9: (2, 0.8),
       10: (1.4, 0.4), 11: (4, 0.62), 12: (5.2, 0.42), 13: (9, 0.5), 14: (7, 0.48), 15: (7.4, 0.25), 16: (5.2, 0.030), 17: (4.1, 0.2), 18: (3.2, 0.020)}

no_final = 18
print("Busca em profundidade:")
visited_with_state_check = set()

chosen_path = dfs_sverificacao(G, node=0, target=no_final, path=[])
print("Caminho escolhido:", chosen_path)

# Draw the graph with node labels and attributes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', arrows=True)

# Create a list of edges for the chosen path
caminho = [(chosen_path[i], chosen_path[i+1]) for i in range(len(chosen_path)-1)]

# Draw the chosen path in red
nx.draw_networkx_edges(G, pos, edgelist=caminho, edge_color='red', width=2)

plt.title("Grafo com Caminho de 0 para 18")
plt.axis('off')
plt.show()
