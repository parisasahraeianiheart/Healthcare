# Healthcare

# Optimization in Healthcare

This repository contains a network optimization model to analyze and improve comorbidity progression in patients, inspired by graduate research.

## Description

The project uses optimization techniques to allocate limited healthcare resources to patients based on their comorbidity progression rates and severity levels. It leverages Python, Gurobi, and network optimization concepts.

## Features
- Analyze patient data to identify critical conditions.
- Optimize treatment allocation to minimize overall progression rates.
- Provide interpretable solutions using network optimization.

## Repository Structure
optimization-in-healthcare/
├── data/
│   └── comorbidity_sample_data.csv       # Sample dataset for comorbidity progression
├── src/
│   ├── network_optimization.py           # Main script for solving the optimization problem
│   ├── data_preprocessing.py             # Script for cleaning and processing data
│   └── utils.py                          # Helper functions (e.g., result visualization)
├── notebooks/
│   └── optimization_demo.ipynb           # Jupyter notebook for detailed explanation and demos
├── requirements.txt                      # List of required libraries
└── README.md                             # Project documentation


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/optimization-in-healthcare.git
   cd optimization-in-healthcare


   python -m venv env
source env/bin/activate  # For MacOS/Linux
env\Scripts\activate     # For Windows
pip install -r requirements.txt


python src/network_optimization.py


jupyter notebook notebooks/optimization_demo.ipynb


---


**`requirements.txt`**
