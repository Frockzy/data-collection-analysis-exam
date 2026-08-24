import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Global Earthquake Tracker", layout="wide")

#fetch earthquake data from USGS API
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
data = response.json()

#extract fields from the data
rows = []
for feature in data['features']:
    properties = feature['properties']
    coordinates = feature['geometry']['coordinates']
    rows.append({
        'Place': properties['place'],
        'Magnitude': properties['mag'],
        'Time': pd.to_datetime(properties['time'], unit='ms'),
        'Longitude': coordinates[0],
        'Latitude': coordinates[1],
        'Depth': coordinates[2]
    })

quake_df = pd.DataFrame(rows)
quake_df['Time'] = pd.to_datetime(quake_df['Time'], unit='ms')
quake_df = quake_df.dropna(subset=['Magnitude', 'Longitude', 'Latitude'])

#risk_category categorization based on magnitude
def categorize_risk(magnitude):
    if magnitude < 3.0:
        return 'Minor'
    elif 3.0 <= magnitude < 4.9:
        return 'Moderate'
    else:
        return 'Strong'

quake_df['risk_category'] = quake_df['Magnitude'].apply(categorize_risk)

print(quake_df.head(20))
print(quake_df.shape)

st.markdown("# Global Earthquake Tracker")
st.markdown("This application shows recent global sismic activity from the past 30 days, sourced from the USGS Earthquake API. You can filter earthquakes by magnitude and risk level.")

#sidebar filters
st.sidebar.header("Filters")
min_magnitude = st.sidebar.slider("Minimum Magnitude", 0.0, 10.0, 0.0)
max_depth = st.sidebar.slider("Maximum Depth (km)", 0, 700, 700)
risk_filter = st.sidebar.multiselect("Risk category", options=['Minor', 'Moderate', 'Strong'], default=['Minor', 'Moderate', 'Strong'])

#apply filters
filtered_quakes = quake_df[
    (quake_df['Magnitude'] >= min_magnitude) &
    (quake_df['Depth'] <= max_depth) &
    (quake_df['risk_category'].isin(risk_filter))
]

#metrics
col1, col2 = st.columns(2)
col1.metric("Total Earthquakes", len(filtered_quakes))
col2.metric("Maximum Magnitude", round(filtered_quakes['Magnitude'].max(), 2))

#map
st.subheader("Earthquake locations")
st.map(filtered_quakes[['Latitude', 'Longitude']].rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'}))