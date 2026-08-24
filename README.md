# data-collection-analysis-exam
# Global Earthquake Tracker Exam Project

## Overview
This repository contains the exam project for the Global Earthquake Tracker application. The application displays recent global seismic activity from the past 30 days using data sourced directly from the USGS Earthquake API, allowing users to filter earthquakes based on magnitude and risk level.

---

## Features & Implementation
- **Interactive Map:** Utilizes `st.map()` to plot filtered earthquake locations onto an interactive world map that updates dynamically based on user interface selections.
- **Dynamic Metrics:** Displays side-by-side metrics above the map using `st.columns()` to show the total number of earthquakes based on active filters and the maximum magnitude for that selection.
- **UI Filters:** Includes responsive sidebar filters allowing users to adjust parameters such as minimum magnitude, maximum depth (km), and risk categories (Minor, Moderate, Strong).

---

## Project Structure
- app.py              # Main Streamlit application script
- requirements.txt    # Project dependencies
- README.md           # Project documentation

---

## Tech Stack
- **Language:** Python
- **Framework:** Streamlit (`st.map()`, `st.columns()`, sidebar components)
- **Data Source:** USGS Earthquake API (past 30 days)

---

## Getting Started

### Prerequisites
Make sure you have Python installed. Clone the repository and install the required dependencies:

git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
pip install -r requirements.txt

### Running the Application
To run the Streamlit app locally, execute:

streamlit run app.py

### Running the Project
- To run the data collection script: python scripts/collect_data.py
- To explore the analysis: Launch Jupyter Notebook and open the files in the notebooks/ folder.
