import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

def apply_clustering(df):
    features = ['age', 'bmi', 'physical_activity', 'sleep_hours', 'stress_level']
    df_cleaned = df.dropna(subset=features)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_cleaned[features])
    
    # Hierarchical Clustering
    linked = linkage(df_scaled, method='ward')
    plt.figure(figsize=(10, 5))
    dendrogram(linked, labels=df_cleaned.index, orientation="top")
    plt.title("Dendrogram for Hierarchical Clustering")
    plt.show()
    
    num_clusters = 4  # Adjust based on dendrogram
    df_cleaned['hierarchical_cluster'] = fcluster(linked, num_clusters, criterion='maxclust')
    
    # Gaussian Mixture Model
    gmm = GaussianMixture(n_components=num_clusters, covariance_type='full', random_state=42)
    gmm.fit(df_scaled)
    df_cleaned['gmm_cluster'] = gmm.predict(df_scaled)
    
    return df_cleaned
