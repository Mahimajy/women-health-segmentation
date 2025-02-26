import pandas as pd
from src.clustering import perform_clustering
from src.recommendations import generate_recommendations

def main():
    # Load dataset
    data_path = "data/health_data.csv"
    df = pd.read_csv(data_path)
    
    # Perform clustering
    clustered_df = perform_clustering(df)
    
    # Generate recommendations
    recommendations_df = generate_recommendations(clustered_df)
    
    # Save results
    results_path = "results/segmented_health_data.csv"
    recommendations_df.to_csv(results_path, index=False)
    print(f"Segmented data saved to {results_path}")

if __name__ == "__main__":
    main()
