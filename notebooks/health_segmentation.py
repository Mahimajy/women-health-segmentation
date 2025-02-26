import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score

# Load clustered data
df = pd.read_csv("results/segmented_health_data.csv")

# Plot cluster distributions
plt.figure(figsize=(8, 5))
sns.countplot(x="gmm_cluster", data=df, palette="Set2")
plt.title("Distribution of GMM Clusters")
plt.xlabel("Cluster")
plt.ylabel("Count")
plt.show()

# Scatter plot of BMI vs. Stress Level by cluster
plt.figure(figsize=(8, 5))
sns.scatterplot(x="bmi", y="stress_level", hue="gmm_cluster", data=df, palette="coolwarm")
plt.title("BMI vs. Stress Level by Cluster")
plt.show()

# Check mean values for each feature within clusters
centroids = df.groupby("gmm_cluster").mean()
print("Cluster Centroids:\n", centroids)

# Plot feature distributions by cluster
features = ["bmi", "stress_level", "age", "sleep_hours"]  # Adjust based on your dataset

for feature in features:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="gmm_cluster", y=feature, data=df, palette="Set2")
    plt.title(f"{feature.capitalize()} Distribution Across Clusters")
    plt.show()



# Compute silhouette score
X = df.drop(columns=["gmm_cluster"])  # Use only numerical features
sil_score = silhouette_score(X, df["gmm_cluster"])
print(f"Silhouette Score: {sil_score:.3f}")



# Save Notebook
print("Notebook ready for further analysis!")
