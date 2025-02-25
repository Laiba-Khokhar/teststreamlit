import streamlit as st
st.title("Welcome  to my code")
name = st.text_input("Enter Your Name")
fname = st.text_input("Enter Your Father Name")
adr = st.text_area("Enter Your Message")
classdata = st.selectbox("Enter Your Class", ["1","2","3","4","5"])
button = st.button('Submit')
if button :
    st.markdown(f"""
    # Name : {name}
    # Father Name : {fname}
    # Address : {adr}
    # Class : {classdata}
    """)
st.balloons()
st.snow()