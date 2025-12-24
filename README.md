# Automobile Sales Analysis During Recession Periods

This project analyzes historical automobile sales data to understand how various recession periods impacted the industry. It provides insights into sales trends, consumer behavior, and the effectiveness of advertising during economic downturns.

## Project Structure
The repository is organized into two main parts:

1. **Analysis & Visualizations (`notebooks/analysis.ipynb`)**: 
   - Uses **Matplotlib** and **Seaborn** to visualize sales fluctuations.
   - Analyzes GDP impact, unemployment rates, and seasonality.
   - Includes correlation studies between advertising expenditure and sales volume.

2. **Interactive Dashboard (`app/dashboard.py`)**:
   - A dynamic web application built with **Dash** and **Plotly**.
   - Allows users to generate "Recession Report Statistics" or "Yearly Report Statistics".
   - Features interactive charts for executive-level decision-making.

## Data Overview
The dataset includes key economic and sales indicators:
- Automobile Sales & Vehicle Types
- GDP & Unemployment Rates
- Consumer Confidence & Seasonality Weights
- Advertising Expenditure & Pricing

## Technologies Used
- Python (Pandas, NumPy)
- Matplotlib & Seaborn (Static Visualization)
- Dash & Plotly (Interactive Dashboard)

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas dash plotly seaborn matplotlib
