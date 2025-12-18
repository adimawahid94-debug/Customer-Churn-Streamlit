import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# ======================
# HEADER
# ======================
st.title("📊 Customer Churn Dashboard")
st.write(
    "Dashboard ini digunakan untuk memahami pola churn pelanggan "
    "dan membantu tim bisnis menentukan strategi retensi."
)

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    return pd.read_csv("bank_churn_data.csv")

df = load_data()
# memastikan kolom churn ada
if "churn" not in df.columns and "attrition_flag" in df.columns:
    df["churn"] = df["attrition_flag"].apply(
        lambda x: 1 if x == "Attrited Customer" else 0
    )

# ======================
# SIDEBAR (INTERAKTIF)
# ======================
st.sidebar.header("Filter Data")

gender_filter = st.sidebar.selectbox(
    "Pilih Gender",
    options=["All"] + sorted(df["gender"].unique().tolist())
)

age_range = st.sidebar.slider(
    "Rentang Usia",
    int(df["customer_age"].min()),
    int(df["customer_age"].max()),
    (25, 50)
)

# ======================
# APPLY FILTER
# ======================
filtered_df = df.copy()

if gender_filter != "All":
    filtered_df = filtered_df[filtered_df["gender"] == gender_filter]

filtered_df = filtered_df[
    (filtered_df["customer_age"] >= age_range[0]) &
    (filtered_df["customer_age"] <= age_range[1])
]

# ======================
# METRICS
# ======================
col1, col2, col3 = st.columns(3)

total_customers = filtered_df.shape[0]
churn_rate = filtered_df["churn"].mean() * 100
avg_age = filtered_df["customer_age"].mean()

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate (%)", f"{churn_rate:.2f}")
col3.metric("Average Age", f"{avg_age:.1f}")

# ======================
# VISUALIZATION
# ======================
st.subheader("Distribusi Churn")

fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x="churn", ax=ax)
ax.set_xticklabels(["Not Churn", "Churn"])
ax.set_xlabel("Status")
ax.set_ylabel("Jumlah Pelanggan")
st.pyplot(fig)
st.subheader("Churn Rate Berdasarkan Gender")

# hitung churn rate per gender
churn_gender = (
    filtered_df
    .groupby("gender")["churn"]
    .mean()
    .reset_index()
)

# ubah ke persen
churn_gender["churn_rate"] = churn_gender["churn"] * 100

# plot
fig, ax = plt.subplots()
sns.barplot(
    data=churn_gender,
    x="gender",
    y="churn_rate",
    ax=ax
)
ax.set_ylabel("Churn Rate (%)")
ax.set_xlabel("Gender")
ax.set_title("Perbandingan Churn Rate berdasarkan Gender")

st.pyplot(fig)

st.caption(
    "Grafik ini membantu melihat apakah terdapat perbedaan tingkat churn "
    "antara pelanggan laki-laki dan perempuan."
)

# ======================
# DATA PREVIEW
# ======================
with st.expander("Lihat Data (Preview)"):
    st.dataframe(filtered_df.head(20))
    st.write(df.columns)

