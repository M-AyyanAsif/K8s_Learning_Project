import streamlit as st
from datetime import date

# 1. Setup page configuration
st.set_page_config(page_title="Age Calculator", layout="centered")

# 2. Load custom CSS for light purple UI and centering
try:
    with open("style.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# 3. Load custom HTML for the center-top placement
try:
    with open("header.html") as html_file:
        st.markdown(html_file.read(), unsafe_allow_html=True)
except FileNotFoundError:
    pass

# 4. Streamlit Form
with st.form("age_calculator_form"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        last_name = st.text_input("Last Name")
        
    st.write("Date of Birth")
    d_col, m_col, y_col = st.columns(3)
    with d_col:
        day = st.number_input("Day", min_value=1, max_value=31, step=1)
    with m_col:
        month = st.selectbox("Month", range(1, 13), format_func=lambda x: date(2000, x, 1).strftime('%B'))
    with y_col:
        year = st.number_input("Year", min_value=1900, max_value=date.today().year, step=1, value=2000)

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if first_name and last_name:
            try:
                # Calculate exact age
                dob = date(year, month, day)
                today = date.today()
                
                # Subtract 1 year if the birthday hasn't happened yet this year
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                
                # Display Results
                st.success("Calculation Successful!")
                st.markdown(f"**Full Name:** {first_name.strip()} {last_name.strip()}")
                st.markdown(f"**Date of Birth:** {dob.strftime('%B %d, %Y')}")
                st.markdown(f"**Exact Age:** {age} years old")
                
            except ValueError:
                st.error("Invalid date selected. Please check the day and month combination (e.g., February 30th is invalid).")
        else:
            st.error("Please enter both First Name and Last Name.")