import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Data Visualization")

df = pd.read_excel("mumbai_flood_ml_dataset_final.xlsx")
df.columns = df.columns.str.strip()

numeric_df = df.select_dtypes(include="number")

# ----------------------------
# Correlation Heatmap
# ----------------------------
st.subheader("Correlation Heatmap")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax1)
st.pyplot(fig1)

# ----------------------------
# Scatter Plot
# ----------------------------
st.subheader("Rainfall vs Flood Severity")

fig2, ax2 = plt.subplots()
sns.scatterplot(
    x=df["Rainfall_mm"],
    y=df["Flood_Severity_Index_0to10"],
    ax=ax2
)
st.pyplot(fig2)