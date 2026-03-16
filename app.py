import streamlit as st
import pandas as pd

st.title("Sustainable Shopping Assistant")

data = pd.read_csv("products.csv")

product = st.text_input("Enter product name")

if product:
    result = data[data["Product"].str.lower() == product.lower()]

    if not result.empty:
        score = result["EcoScore"].values[0]
        alt = result["Alternative"].values[0]

        st.write("Eco Score:", score)

        if score < 50:
            st.warning("Low sustainability product")

        st.write("Better Alternative:", alt)

    else:
        st.write("Product not found")