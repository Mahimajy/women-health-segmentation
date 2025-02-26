def generate_recommendations(cluster):
    if cluster == 0:
        return "Prioritize balanced diet and mild physical activity."
    elif cluster == 1:
        return "Improve sleep patterns and reduce stress."
    elif cluster == 2:
        return "Increase physical activity and maintain hydration."
    else:
        return "Regular health check-ups and mindful stress management."
