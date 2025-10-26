import networkx as nx
import numpy as np
import random
import time

def compute_basic_metrics(G, sample_size=None):
    """
    Compute main graph metrics as required in the Resilient Networks project.
    For small graphs, full metrics are calculated.
    For large graphs, the average shortest path is approximated using random sampling.
    """

    print("📊 Calculating basic network metrics...")
    start = time.time()

    # --- Connected components ---
    comps = [len(c) for c in nx.connected_components(G)]
    giant = G.subgraph(max(nx.connected_components(G), key=len)).copy()

    print(f"🧩 Number of connected components: {len(comps)}")
    print(f"🧠 Giant component size: {max(comps)} nodes")

    # --- Average shortest path length (full or approximate) ---
    print("⏳ Approximating average shortest path length on the giant component...")
    nodes = list(giant.nodes())

    if sample_size is None or len(nodes) <= sample_size:
        print("🔹 Using all nodes to calculate the exact average shortest path length.")
        avg_path = nx.average_shortest_path_length(giant)
    else:
        print(f"🔹 Using a random sample of {sample_size} nodes for approximation.")
        sample = random.sample(nodes, sample_size)
        total = 0
        count = 0
        for i, s in enumerate(sample, 1):
            sp = nx.single_source_shortest_path_length(giant, s)
            total += sum(sp.values())
            count += len(sp)
            if i % 100 == 0 or i == len(sample):
                print(f"   ➜ Processed {i}/{sample_size} sample nodes...")
        avg_path = total / count

    print("✅ Average shortest path length computed.\n")

    # --- Degree metrics (for Power-law properties) ---
    degrees = [d for _, d in G.degree()]
    avg_degree = np.mean(degrees)
    max_degree = np.max(degrees)
    print(f"📈 Average degree: {avg_degree:.2f}, Max degree: {max_degree}")

    # --- Clustering and Assortativity ---
    avg_clust = nx.average_clustering(G)
    assort = nx.degree_assortativity_coefficient(G)
    print(f"🔗 Average clustering coefficient: {avg_clust:.4f}")
    print(f"🔄 Degree assortativity: {assort:.4f}")

    # --- Density ---
    density = nx.density(G)
    print(f"🌐 Graph density: {density:.6f}")

    # --- Metrics dictionary ---
    metrics = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": density,
        "avg_clustering": avg_clust,
        "assortativity": assort,
        "components": len(comps),
        "giant_component_size": max(comps),
        "avg_shortest_path_on_giant": avg_path,
        "avg_degree": avg_degree,
        "max_degree": max_degree
    }

    print(f"✅ Basic metrics computed successfully in {time.time() - start:.2f} seconds!\n")
    return metrics
