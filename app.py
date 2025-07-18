import streamlit as st
import pandas as pd
import requests

@st.cache_data
def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/public-datasets-coding/code-snippets/main/code_library.csv")
    return data

data = load_data()

st.set_page_config(page_title="My Code Assistant", layout="centered")
st.title("🧠 My Personal Code Assistant")
st.markdown("Search Excel formulas, VBA, Python snippets — or ask any coding query!")

query = st.text_input("🔍 Enter your query:", placeholder="e.g. Python remove duplicates, Excel sum last row")

if query:
    query_lower = query.lower()
    filtered = data[data['content'].str.lower().str.contains(query_lower)]

    if not filtered.empty:
        st.subheader("📄 Results from Local Code Library")
        for _, row in filtered.iterrows():
            st.markdown(f"**📁 {row['category']} | 📌 {row['title']}**")
            st.code(row['content'], language=row['language'])
    else:
        st.info("No direct match found in local library. Fetching online sources will be added next.")
else:
    st.warning("Type a prompt to begin searching.")
