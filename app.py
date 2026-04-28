import streamlit as st
import pandas as pd
from database import insert_data, get_all_data
from utils import clean_text, is_similar

st.set_page_config(page_title="Data Redundancy System", layout="centered")

st.title("🧠 Data Redundancy Removal System")

menu = ["Add Data", "View Data"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- ADD DATA ----------------
if choice == "Add Data":
    st.subheader("Add New Data")

    user_input = st.text_area("Enter Data")

    if st.button("Submit"):
        cleaned_input = clean_text(user_input)
        existing_data = get_all_data()

        existing_texts = [clean_text(d[1]) for d in existing_data]

        # Exact duplicate check
        if cleaned_input in existing_texts:
            st.error("❌ Exact Duplicate Found")

        # Similarity check
        elif is_similar(cleaned_input, existing_data):
            st.warning("⚠️ Similar Data Detected (Possible Redundancy)")

        else:
            if insert_data(cleaned_input):
                st.success("✅ Data Stored Successfully")
            else:
                st.error("Something went wrong")


# ---------------- VIEW DATA ----------------
elif choice == "View Data":
    st.subheader("Stored Data")

    data = get_all_data()

    if data:
        df = pd.DataFrame(data, columns=["ID", "Content"])
        st.dataframe(df)
    else:
        st.info("No data available")