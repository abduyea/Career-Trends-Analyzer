# Career Trends Analyzer

A data-driven project that analyzes LinkedIn job posting (2023-2024) datasets to identify in-demand technical and professional skills, salary patterns, and regional/industry trends. The workflow includes structured data cleaning, exploratory analysis, skill extraction, and preparation of final datasets for visualization.

## Overview

This project focuses on:

- Identifying top technical and professional skills
- Detecting skill gaps across industries
- Analyzing salaries, job types, experience levels
- Comparing trends by region and industry
- Producing clean datasets and visualizations

## Setup

### Option 1 — Google Colab

1. Open the notebook in Colab
2. Mount Google Drive if needed
3. Run cells in order

### Option 2 — Local Environment

```bash
git clone https://github.com/abduyea/Career-Trends-Analyzer.git
cd Career-Trends-Analyzer
conda env create -f requirements.yml
conda activate career-trends-analyzer
```

## How to Use

Run notebooks in sequence:

1. **Project_setup.ipynb** - Initial setup and configuration
2. **data_ingestion.ipynb** - Load and validate data
3. **data_cleaning_and preprocessing.ipynb** - Clean and prepare data
4. **skill_analysis.ipynb** - Analyze in-demand skills
5. **salary_analysis.ipynb** - Analyze salary patterns
6. **industry_and_regional_trends.ipynb** - Analyze trends by industry and region
7. **sentiment_analysis.ipynb** - Analyze sentiment of job descriptions
8. **visualizations_and_dashboards.ipynb** - Create visualizations

   
the link for the data set : https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/versions/7/data

## Project Structure

Career-Trends-Analyzer/
├── README.md
├── requirements.yml
├── data/
│   ├── raw/
│   │   ├── companies/
│   │   ├── jobs/
│   │   ├── mappings/
│   │   └── postings.csv
│   └── processed/
├── notebooks/
│   ├── Project_setup.ipynb
│   ├── data_ingestion.ipynb
│   ├── data_cleaning_and preprocessing.ipynb
│   ├── skill_analysis.ipynb
│   ├── salary_analysis.ipynb
│   ├── industry_and_regional_trends.ipynb
│   ├── sentiment_analysis.ipynb
│   └── visualizations_and_dashboards.ipynb
├── src/
│   └── utils/
│       ├── config.py
│       └── data_loader.py
└── report/
```

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter

All dependencies listed in `requirements.yml`

