import streamlit as st

def largest_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Largest of Three Numbers")

# Create a form for user input
with st.form("input_form"):

    # Take user input
    num1 = st.number_input("Enter 1st number:", step=1, format="%d")
    num2 = st.number_input("Enter 2nd number:", step=1, format="%d")
    num3 = st.number_input("Enter 3rd number:", step=1, format="%d")
    
    # Create a submit button
    submit_button = st.form_submit_button("Find Largest")
    
    # Find the largest number on button click
    if submit_button:
        max_num = largest_num(num1, num2, num3)
        st.write(f"The largest number is {max_num}.")
