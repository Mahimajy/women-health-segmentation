import pandas as pd

def generate_recommendations(df):
    # Ensure the cluster column exists
    if "gmm_cluster" not in df.columns:
        raise ValueError("Missing 'gmm_cluster' column in DataFrame")

    recommendations = []

    # Define personalized recommendations based on clusters
    for _, row in df.iterrows():
        cluster = row["gmm_cluster"]

        if cluster == 0:
            recommendation = "Focus on mental well-being and stress management"
        elif cluster == 1:
            recommendation = "Maintain balanced nutrition and regular exercise"
        elif cluster == 2:
            recommendation = "Increase physical activity and improve sleep habits"
        elif cluster == 3:
            recommendation = "Monitor BMI and schedule regular health checkups"
        else:
            recommendation = "General wellness recommendations"

        recommendations.append(recommendation)

    # Add recommendations to DataFrame
    df["personalized_recommendation"] = recommendations
    return df
