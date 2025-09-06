import streamlit as st
st.title("Project health data")
st.header("BMI Calculator")
st.subheader("Because that hasn't been done before...")
if st.button("Calculate BMI Now"):

    gender = st.radio("Select gender:", ['Female','Male'])
    if gender == 'Male':
        st.succcess("Male confirmed")
    elif gender == "Female":
        st.success("Female confirmed")
    else:
        st.error("")

else:
    options = st.selectbox("Select an option", ['About', 'Data analysis', 'Plans'])


