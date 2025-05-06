
import streamlit as st

st.title("ASM Civil Suppliers and Earthmovers")


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assests/Lorryplant2.png",width=230)

with col2:
    st.title("MoulishKumar", anchor=False)
    st.write("I am running this business more than 15 years. Sand is a crucial material in construction and other industries, making efficient transportation vital."
          "We promising with good quality and reasonable price for our valuable customer.")

    phone_number = "+91 7708793702"
    if st.button("Call me", key="green"):
        st.markdown(f'''
                <a href="tel:{phone_number}">
                    <button style="padding: 10px 20px; font-size: 20px;">📞 Call {phone_number}</button>
                </a>
                ''', unsafe_allow_html=True)

