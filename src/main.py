import pandas as pd
from src.load_graphs import load_zeroaccess, load_roadnet
from src.metrics import compute_basic_metrics
from src.robustness import robustness_curve
from src.plots import plot_degree_hist, plot_robustness
import time

print("🚀 Starting Resilient Networks Analysis...\n")

# === STEP 1: LOAD DATA ===
start_time = time.time()
print("📂 Loading ZeroAccess P2P Botnet graph...")
G1 = load_zeroaccess("../data/za_16464_all_max.graphml.gz")
print(f"✅ ZeroAccess loaded successfully: {G1.number_of_nodes():,} nodes, {G1.number_of_edges():,} edges\n")

print("📂 Loading Road Network graph (roadNet-CA)... This might take a few minutes...")
G2 = load_roadnet("../data/roadNet-CA.txt.gz")
print(f"✅ RoadNet loaded successfully: {G2.number_of_nodes():,} nodes, {G2.number_of_edges():,} edges\n")
print(f"⏱️ Total loading time: {time.time() - start_time:.2f} seconds\n")

# === STEP 2: COMPUTE METRICS ===
print("📊 Calculating basic network metrics...")
# For ZeroAccess -> use all nodes (sample_size=None)
m1 = compute_basic_metrics(G1, sample_size=500) #10K nodes

# For RoadNet-CA -> use a sample of 2000 nodes
m2 = compute_basic_metrics(G2, sample_size=2000) #≈2M nodes

metrics_df = pd.DataFrame([m1, m2], index=["ZeroAccess", "RoadNet"])
metrics_df.to_csv("../results/metrics_summary.csv")
print("✅ Metrics calculated and saved to 'results/metrics_summary.csv'\n")

# === STEP 3: DEGREE DISTRIBUTIONS ===
print("📈 Plotting degree distributions (log–log)...")
plot_degree_hist(G1, "ZeroAccess", "../results/figures/zeroaccess_degree.png")
plot_degree_hist(G2, "RoadNet-CA", "../results/figures/roadnet_degree.png")
print("✅ Degree distribution plots saved in 'results/figures/'\n")

# === STEP 4: ROBUSTNESS EXPERIMENTS ===
print("🧩 Running robustness experiments (random vs targeted attacks)...")
curves1 = {
    "Random": robustness_curve(G1, "random"),
    "Degree": robustness_curve(G1, "degree")
}
plot_robustness(curves1, "ZeroAccess", "../results/figures/zeroaccess_robustness.png")

curves2 = {
    "Random": robustness_curve(G2, "random"),
    "Degree": robustness_curve(G2, "degree")
}
plot_robustness(curves2, "RoadNet-CA", "../results/figures/roadnet_robustness.png")
print("✅ Robustness plots created successfully!\n")

# === STEP 5: COMPLETION ===
print("🎉 All analysis steps completed successfully!")
print("📁 Results are saved in the 'results/' folder:")
print("   - CSV metrics file: results/metrics_summary.csv")
print("   - Figures: results/figures/*.png\n")
print("✅ Program finished without errors. You can now use these results in your report.")
