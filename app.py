import streamlit as st

# Title and basic text output
st.title('My First Streamlit App')
st.header('Welcome to Streamlit!')
st.write('This is a simple example to demonstrate Streamlit basics.')

# Input fields
user_name = st.text_input('Enter your name', 'Type Here...')
user_age = st.number_input('Enter your age', min_value=0, max_value=150, value=25)

# Display output based on input
if st.button('Submit'):
    st.write(f'Hello {user_name}, you are {user_age} years old.')
