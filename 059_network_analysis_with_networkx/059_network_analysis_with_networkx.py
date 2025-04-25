import networkx as nx
import matplotlib.pyplot as plt

def network_analysis_with_networkx():
    # Create a simple graph
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])

    # Calculate degree centrality
    degree_centrality = nx.degree_centrality(graph)
    print("Degree Centrality:", degree_centrality)

    # Draw the graph
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=800,
            font_size=12, font_weight='bold')
    plt.title("Simple Graph")
    plt.savefig("simple_graph.png")
    print("Simple graph saved to simple_graph.png")

network_analysis_with_networkx()
