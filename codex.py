#importing streamlit 
import streamlit as st 

#Displaying text
names = ['omar','ali','ahmed']
st.title('recap on streamlit')
st.header('this is a header')
st.subheader('this is a subheader')
st.text(names)
st.write(names)

#step 4: displaying info massege 
st.error('An error occured')
st.warning('A warning message')
st.success('A success message')
st.info('Note: our restaurant closes at 10 pm')

#Inputs(
name = st.text_input('enter your name')
age = st.number_input(
    'Enter your age ',
    min_value=0,
    max_value=100,
    value=20,
    step=1
)


if st.button('display info'):
    st.write(f'your name is {name} and your age is {age}')