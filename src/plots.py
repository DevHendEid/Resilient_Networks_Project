import matplotlib.pyplot as plt

def plot_degree_hist(G, title, save_path):
    degs = [d for _, d in G.degree()]
    plt.figure()
    plt.hist(degs, bins=100)
    plt.xscale('log'); plt.yscale('log')
    plt.title(title + " Degree Distribution")
    plt.xlabel("Degree"); plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(save_path)

def plot_robustness(curves, title, save_path):
    plt.figure()
    for label, data in curves.items():
        plt.plot(data[:,0]*100, data[:,1], label=label)
    plt.xlabel("% Nodes Removed")
    plt.ylabel("Largest Connected Component Size")
    plt.title(title + " – Robustness")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
