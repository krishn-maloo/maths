import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

# Add edges to the graph
G.add_edge(0, 1, weight=6)
G.add_edge(0, 3, weight=6)
G.add_edge(0, 2, weight=8)
G.add_edge(1, 3, weight=5)
G.add_edge(1, 4, weight=10)
G.add_edge(2, 3, weight=7)
G.add_edge(2, 4, weight=5)
G.add_edge(2, 5, weight=3)
G.add_edge(4, 5,weight= 3)
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color="blue",node_size=2000,with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})

# Show the plot
plt.show()

n=nx.single_source_dijkstra(G,source=0,target=5)
print(n)
