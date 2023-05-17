import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def generate_sparse_graph(n):
    # Create an empty graph with n nodes
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Add random edges until the graph is connected
    while not nx.is_connected(G):
        # Add random edge between two nodes from different connected components
        components = list(nx.connected_components(G))
        node1 = random.choice(list(components[0]))
        node2 = random.choice(list(components[1]))
        G.add_edge(node1, node2)

    return G

def generate_dense_graph(n):
    # Create a complete graph
    G = nx.complete_graph(n)

    # Remove random edges
    edges = list(G.edges())
    random.shuffle(edges)
    num_edges_to_remove = int(0.2 * n * (n - 1) / 2)  # Adjust the density as desired
    edges_to_remove = edges[:num_edges_to_remove]
    G.remove_edges_from(edges_to_remove)

    return G

def plot_graph(G):
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', width=1.0)
    plt.show()


def dijkstra(G):
    start_time = time.time()
    # find all pairs of shortest paths
    shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

    return time.time() - start_time + 0.1

def floyd(G):
    start_time = time.time()
    # find all pairs of shortest paths
    shortest_paths = dict(nx.floyd_warshall(G))
    return time.time() - start_time + 0.1


def run(n):
    sparse_graph = generate_sparse_graph(n)
    dense_graph = generate_dense_graph(n)

    d1 = dijkstra(sparse_graph)
    f1 = floyd(sparse_graph)

    print("SPARSE GRAPH, n =", n)
    print("Dijkstra time:", d1)
    print("Floyd-Warshall time:", f1)

    d2 = dijkstra(dense_graph)
    f2 = floyd(dense_graph)

    print("\n")
    print("DENSE GRAPH, n =", n)
    print("Dijkstra time:", d2)
    print("Floyd-Warshall time:", f2)

    return d1, f1, d2, f2


n = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

dijkstra_time_sparse = []
floyd_time_sparse = []

dijkstra_time_dense = []
floyd_time_dense = []


for i in n:
    result = run(i)

    dijkstra_time_sparse.append(result[0])
    floyd_time_sparse.append(result[1])

    dijkstra_time_dense.append(result[2])
    floyd_time_dense.append(result[3])

print("\n\n")
print(dijkstra_time_sparse)
print(floyd_time_sparse)
print("\n")
print(dijkstra_time_dense)
print(floyd_time_dense)


# Plotting sparse results
plt.figure(figsize=(8, 6))
plt.plot(n, dijkstra_time_sparse, label='Dijkstra')
plt.plot(n, floyd_time_sparse, label='Floyd-Warshall')
plt.xlabel('Number of vertices')
plt.ylabel('Time')
plt.title('Sparse Graph Results')
plt.legend()
plt.grid(True)
plt.show()

# Plotting dense results
plt.figure(figsize=(8, 6))
plt.plot(n, dijkstra_time_dense, label='Dijkstra')
plt.plot(n, floyd_time_dense, label='Floyd-Warshall')
plt.xlabel('Number of vertices')
plt.ylabel('Time')
plt.title('Dense Graph Results')
plt.legend()
plt.grid(True)
plt.show()

