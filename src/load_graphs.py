import gzip
import networkx as nx
import time

# =========================================================
# 🕸️ Load the ZeroAccess (P2P Botnet) graph
# =========================================================
def load_zeroaccess(path):
    print(f"📂 Loading ZeroAccess P2P Botnet graph from file: {path}")
    start = time.time()

    # Read GraphML file (compressed with gzip)
    with gzip.open(path, "rt") as f:
        G = nx.read_graphml(f)

    # Convert to undirected graph if necessary
    if G.is_directed():
        G = G.to_undirected()

    print("✅ ZeroAccess graph loaded successfully!")
    print(f"   Number of nodes: {G.number_of_nodes():,}")
    print(f"   Number of edges: {G.number_of_edges():,}")
    print(f"⏱️ Loading time: {time.time() - start:.2f} seconds\n")
    return G


# =========================================================
# 🛣️ Load the Road Network (roadNet) graph
# =========================================================
def load_roadnet(path):
    print(f"📂 Reading Road Network file: {path}")
    start = time.time()
    G = nx.Graph()
    count = 0

    # Read the compressed edge list line by line
    with gzip.open(path, "rt") as f:
        for line in f:
            # Skip comments or empty lines
            if line.startswith("#") or not line.strip():
                continue

            parts = line.strip().split()
            if len(parts) < 2:
                continue

            u, v = parts[0], parts[1]
            G.add_edge(u, v)
            count += 1

            # Print progress every 100,000 edges
            if count % 100000 == 0:
                print(f"📊 Processed {count:,} edges so far...")

    print("✅ Road Network graph loaded successfully!")
    print(f"   Number of nodes: {G.number_of_nodes():,}")
    print(f"   Number of edges: {G.number_of_edges():,}")
    print(f"⏱️ Loading time: {time.time() - start:.2f} seconds\n")
    return G
