import streamlit as st

placeholder = st.empty()
actual_email = "email"
actual_password = "password"

with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    if email == '':
        st.error('Please input email')
    elif password == '':
        st.error('Please input password')
    elif email == actual_email and password == actual_password:
        placeholder.empty()
        st.success("Login successful")
    else:
        st.error("Login failed")