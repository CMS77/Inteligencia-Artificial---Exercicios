import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

arestas = [(0, 1), (0, 2), (1, 4), (1, 3), (2, 5), (2, 6), (4, 9), (4, 10), (3, 8), (3, 7), (5, 11), (5, 12), (6, 14), (6, 13), (8, 18), (8, 17), (7, 16), (7, 15),
           (7, 12), (12, 7), (14, 12), (16, 18), (17, 7)]
G.add_edges_from(arestas)

pos = {0: (4.2, 0.8), 1: (2.8, 0.6), 2: (6, 0.9), 3: (3.3, 0.36), 4: (1, 0.65), 5: (5.8, 0.67), 6: (7.7, 0.7), 7: (5.5, 0.25), 8: (2.3, 0.19), 9: (2, 0.8),
       10: (1.4, 0.4), 11: (4, 0.62), 12: (5.2, 0.42), 13: (9, 0.5), 14: (7, 0.48), 15: (7.4, 0.25), 16: (5.2, 0.030), 17: (4.1, 0.2), 18: (3.2, 0.020)}

nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', arrows=True)

plt.title("Grafo com Caminho de 0 para 18")
plt.axis('off')
plt.show()


