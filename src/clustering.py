import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.mixture import GaussianMixture

def perform_clustering(df):
    # Select relevant features
    features = ["age", "bmi", "physical_activity", "sleep_hours", "stress_level", "mental_health_score"]
    
    # Drop missing values
    df_cleaned = df.dropna(subset=features)
    
    # Standardize features
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_cleaned[features])

    # Hierarchical Clustering
    linked = linkage(df_scaled, method="ward")
    num_clusters = 4  # Based on dendrogram analysis
    df_cleaned["hierarchical_cluster"] = fcluster(linked, num_clusters, criterion="maxclust")

    # Gaussian Mixture Model (GMM) Clustering
    gmm = GaussianMixture(n_components=num_clusters, covariance_type="full", random_state=42)
    df_cleaned["gmm_cluster"] = gmm.fit_predict(df_scaled)

    return df_cleaned
