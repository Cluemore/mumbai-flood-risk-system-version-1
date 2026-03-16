import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.title("🗺 Mumbai Flood Map")

# Mumbai center coordinates
mumbai_center = [19.0760, 72.8777]

m = folium.Map(location=mumbai_center, zoom_start=11)

# Load dataset
df = pd.read_excel("mumbai_flood_ml_dataset_final.xlsx")
df.columns = df.columns.str.strip()

# Dummy coordinates for demo (You can improve later)
area_coords = {
    "Andheri": [19.1136, 72.8697],
    "Bandra": [19.0607, 72.8365],
    "Colaba": [18.9067, 72.8147],
    "Kurla": [19.0728, 72.8826],
    "Dadar": [19.0176, 72.8562],
    "Sion": [19.0474, 72.8610],
    "Chembur": [19.0626, 72.9005],
    "Ghatkopar": [19.0790, 72.9080],
    "Mulund": [19.1726, 72.9560],
    "Borivali": [19.2290, 72.8570]
}

for _, row in df.iterrows():
    area = row["Area"]
    severity = row["Flood_Severity_Index_0to10"]

    if area in area_coords:
        color = "green"
        if severity >= 6:
            color = "red"
        elif severity >= 3:
            color = "orange"

        folium.CircleMarker(
            location=area_coords[area],
            radius=8,
            popup=f"{area} - Severity: {severity}",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(m)

st_folium(m, width=900, height=600)