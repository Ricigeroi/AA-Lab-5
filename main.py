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
    print("Floyd-marshall time:", f1)

    d2 = dijkstra(dense_graph)
    f2 = floyd(dense_graph)

    print("\n")
    print("DENSE GRAPH, n =", n)
    print("Dijkstra time:", d2)
    print("Floyd-marshall time:", f2)

    return d1, f1, d2, f2


print(run(500))


