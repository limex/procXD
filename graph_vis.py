"""example script to visualize a networkx graph using procXD."""

import networkx as nx
from procXD import SketchBuilder
import csv

if __name__ == "__main__":
    # Read data from CSV file
    try:
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            data = list(reader)
    except FileNotFoundError:
        print("Error: File 'data.csv' not found.")
        exit(1)
    except Exception as e:
        print(f"Error: Failed to read data from CSV file. {e}")
        exit(1)

    # Create a directed graph
    G = nx.DiGraph()
    for row in data:
        source = row[0]
        target = row[2]
        relation = row[1]
        G.add_node(source)
        G.add_node(target)
        G.nodes[source]['label'] = f'N {source}'
        G.nodes[target]['label'] = f'N {target}'
        G.add_edge(source, target, label=relation)
    
    # Visualize the graph
    pos = nx.circular_layout(G) 
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-circular.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.shell_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-shell.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    """
    pos = nx.planar_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-planar.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)
    """
    pos = nx.random_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-random.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.spring_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-spring.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.spectral_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-spectral.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.kamada_kawai_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-kk.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.fruchterman_reingold_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-fr.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

    pos = nx.spiral_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-spiral.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)
    """
    pos = nx.multipartite_layout(G)
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-multip.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)
    """
    pos = nx.bipartite_layout(G, G.nodes())
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G,'Rectangle')
    SAVE_FILE = "results/graph-bip.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)
