import networkx as nx
import random
import numpy as np

def robustness_curve(G, attack="random", steps=30):
    """
    Simulates network robustness under random or targeted (degree-based) attacks.
    Returns an array of (fraction_removed, largest_component_size).
    """

    H = G.copy()
    n = H.number_of_nodes()
    sizes = []

    # Determine removal order
    if attack == "random":
        order = list(H.nodes())
        random.shuffle(order)
    elif attack == "degree":
        order = sorted(H.nodes(), key=lambda x: H.degree(x), reverse=True)
    else:
        raise ValueError("Attack must be 'random' or 'degree'.")

    chunk = max(1, n // steps)
    removed = 0

    for i in range(n):
        # Remove one node
        v = order.pop(0)
        H.remove_node(v)
        removed += 1

        # Recompute degree order dynamically for degree-based attack
        if attack == "degree" and removed % chunk == 0 and len(H) > 0:
            order = sorted(H.nodes(), key=lambda x: H.degree(x), reverse=True)

        # Record component size every 'chunk' removals
        if removed % chunk == 0 or removed == n:
            if H.number_of_nodes() > 0:
                s = len(max(nx.connected_components(H), key=len))
            else:
                s = 0
            sizes.append((removed / n, s))

            # Print progress
            if attack == "degree":
                print(f"⚙️ Degree attack progress: removed {removed}/{n} nodes")
            elif attack == "random":
                print(f"🎲 Random attack progress: removed {removed}/{n} nodes")

    print(f"✅ Finished {attack} attack simulation.\n")
    return np.array(sizes)
