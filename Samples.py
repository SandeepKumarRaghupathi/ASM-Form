import streamlit as st

st.title("Samples")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assests/Lorryplant1.png",width=230)

with col2:
    st.image("./assests/Lorryplant2.png",width=230)


