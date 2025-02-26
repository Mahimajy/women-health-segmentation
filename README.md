# Women’s Health Segmentation

## Overview
This project segments women based on health-related attributes using **Hierarchical Clustering** and **Gaussian Mixture Models (GMM)**. The goal is to provide **personalized healthcare recommendations** based on clustering insights.

## Directory Structure
```
women-health-segmentation/
├── .gitignore
├── README.md
├── data/
│   └── health_data.csv  # Input dataset
├── main.py  # Main execution script
├── notebooks/
│   └── health_segmentation.ipynb  # Exploratory analysis & visualization
├── requirements.txt  # Required dependencies
├── results/
│   └── segmented_health_data.csv  # Clustered output
└── src/
    ├── clustering.py  # Clustering logic
    └── recommendations.py  # Recommendation generation
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/Mahimajy/women-health-segmentation.git
cd women-health-segmentation
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Run Clustering & Recommendations
```bash
python main.py
```
- This script loads `health_data.csv`, performs clustering, and generates `segmented_health_data.csv`.

### Run Jupyter Notebook for Analysis
```bash
jupyter notebook notebooks/health_segmentation.ipynb
```
- Visualizes clustering results and data insights.

## Expected Output
- `results/segmented_health_data.csv`: Dataset with cluster labels.
- Visualizations in `notebooks/health_segmentation.ipynb`.

## Next Steps
- Improve clustering performance by optimizing feature selection.
- Expand dataset with real-world health parameters.
- Implement a web-based dashboard for interactive recommendations.

## Contributing
- Feel free to fork and submit pull requests.
- Open issues for feature suggestions or bugs.
