import pandas as pd
from src.clustering import apply_clustering
from src.recommendations import generate_recommendations

def main():
    # Load dataset
    df = pd.read_csv("data/health_data.csv")
    
    # Apply clustering
    df_clustered = apply_clustering(df)
    
    # Generate recommendations
    df_clustered['recommendation'] = df_clustered['gmm_cluster'].apply(generate_recommendations)
    
    # Save results
    df_clustered.to_csv("results/segmented_health_data.csv", index=False)
    print("Segmentation and recommendations saved successfully.")

if __name__ == "__main__":
    main()
