import matplotlib.pyplot as plt
import networkx as nx
import math

def draw_custom_weighted_graph(node_list, edge_weight_list, edge_route = [], figsize=(30,30)):
    """
    Draw a custom weighted graph with two different styles for edges based on their weights.
    Code based on the code available on: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    
    Parameters:
    node_list (list): A list of nodes in the graph.
    edge_weight_list (list of tuples): A list of edges with weights, where each edge is represented as (node1, node2, weight).
    """
    plt.figure(figsize=figsize)
    # Create the graph
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from(node_list)

    # Add edges with weights
    for (u, v, w) in edge_weight_list:
        if w == math.inf:
            continue
        if ((u,v) in edge_route) or ((v,u) in edge_route):
            G.add_edge(u, v, chosen = 1, weight=w)
        else:
            G.add_edge(u, v, chosen = 0, weight=w)

    # Separate the edges into large and small weight groups
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["chosen"] == 1]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["chosen"] == 0]

    # Get positions for all nodes - using a fixed seed for reproducibility
    pos = nx.circular_layout(G, scale=1)

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=1000)

    # Draw the edges with weights > 0.5
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)

    # Draw the edges with weights <= 0.5 in blue, dashed style
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=30, font_family="sans-serif")

    # Draw edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20)

    # Set margins and display options
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    

def draw_custom_weighted_graph_double(node_list, edge_weight_list, edge_route = [], optimal_route = [], figsize=(30,30)):
    """
    Draw a custom weighted graph with two different styles for edges based on their weights.
    Code based on the code available on: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    
    Parameters:
    node_list (list): A list of nodes in the graph.
    edge_weight_list (list of tuples): A list of edges with weights, where each edge is represented as (node1, node2, weight).
    """
    plt.figure(figsize=figsize)
    # Create the graph
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from(node_list)

    # Add edges with weights
    for (u, v, w) in edge_weight_list:
        if (((u,v) in edge_route) or ((v,u) in edge_route)) and (((u,v) in optimal_route) or ((v,u) in optimal_route)):
            G.add_edge(u, v, chosen = 1, weight=w)
        elif (((u,v) in edge_route) or ((v,u) in edge_route)):
            G.add_edge(u, v, chosen = 2, weight=w)
        else:
            G.add_edge(u, v, chosen = 0, weight=w)

    # Separate the edges into large and small weight groups
    eoptimal = [(u, v) for (u, v, d) in G.edges(data=True) if d["chosen"] == 2]
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["chosen"] == 1]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["chosen"] == 0]

    # Get positions for all nodes - using a fixed seed for reproducibility
    pos = nx.circular_layout(G, scale=1)

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=1000)

    # Draw the edges with weights > 0.5
    nx.draw_networkx_edges(G, pos, edgelist=eoptimal, width=6, edge_color="r")
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)

    # Draw the edges with weights <= 0.5 in blue, dashed style
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=30, font_family="sans-serif")

    # Draw edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20)

    # Set margins and display options
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()