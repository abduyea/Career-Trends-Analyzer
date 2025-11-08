[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<abduyea>/Career-Trends-Analyzer/blob/main/CareerTrends_Analysis.ipynb)

# Career Trends Analyzer

## Overview

Career Trends Analyzer is a data analytics project designed to identify and visualize in-demand technical and professional skills using job posting data. The project focuses on structured data processing, exploratory analysis, and visualization for data-driven insights.

## Directory Structure

CareerTrends_Analyzer/
│
├── data/ # Datasets (compressed if large)
├── postings.zip
├── job_titles.csv
├── company_profiles.csv
├── locations.csv
├── industries.csv
├── education_levels.csv
├── salaries.csv
├── job_descriptions.csv
├── skills.csv
├── experience_levels.csv
└── job_types.csv

│
├── notebooks/ # Main analysis notebooks
│ └── CareerTrends_Analyzer.ipynb
│
├── src/ # Source code modules
│ ├── data_processing.py
│ ├── visualization.py
│ └── utils.py
│
├── reports/ # Output reports and figures
│
├── README.md # Project documentation
└── requirements.txt # Dependencies list

````

## Setup and Usage
1. Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com).
2. Select the **GitHub** tab → paste your repository URL.
3. Open `notebooks/CareerTrends_Analyzer.ipynb`.
4. Optionally, clone the repo directly:
   ```python
   !git clone https://github.com/<your-username>/CareerTrends_Analyzer.git
   %cd CareerTrends_Analyzer
````

5. Run the analysis:
   ```python
   import pandas as pd
   df = pd.read_csv('data/postings.zip', compression='zip')
   df.head()
   ```

---

### 2. Use with Google Drive

1. Upload `postings.zip` to a Drive folder.
2. In Colab:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   df = pd.read_csv('/content/drive/My Drive/CareerTrends_Data/postings.zip', compression='zip')
   ```

---

### 3. Use on GitHub

- The compressed dataset (`data/postings.zip`, ~72 MB) is stored safely under 100 MB.
- Pull the repository:
  ```bash
  git clone https://github.com/<your-username>/CareerTrends_Analyzer.git
  cd CareerTrends_Analyzer
  ```

---

### 4. Run Locally

```bash
git clone https://github.com/<your-username>/CareerTrends_Analyzer.git
cd CareerTrends_Analyzer
pip install -r requirements.txt
python src/data_processing.py
```
