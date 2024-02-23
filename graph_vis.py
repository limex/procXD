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
        target = row[1]
        G.add_edge(source, target)

    # Visualize the graph
    pos = nx.circular_layout(G)
    for node in G.nodes():
        G.nodes[node]['label'] = f'Node {node}'
        G.nodes[node]['pos'] = pos[node]
    sketch_builder = SketchBuilder()
    sketch_builder.render_networkx_graph(G)
    SAVE_FILE = "results/graph.excalidraw"
    sketch_builder.export_to_file(save_path=SAVE_FILE)

