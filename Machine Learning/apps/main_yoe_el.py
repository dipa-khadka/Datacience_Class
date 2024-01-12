import pickle
import numpy as np
with open('model_yoe_el.pickle','rb') as file:
    model = pickle.load(file)
    
import streamlit as st
yoe = st.text_input("Year's of Exprience : ")
edu_level = st.selectbox("Education Level : ",["Bachelor's","Master's","PhD"])

# converting categorical variable to numerical using label encoding
edu_mapping = {"Bachelor's":0,"Master's":1, "PhD":2}
edu_level_numeric = edu_mapping.get(edu_level,0)

if st.button('Submit',type="primary"):
    # Providing input data in the correct format
    input_data = np.array([[int(yoe),edu_level_numeric]])
    
    # Reshape the input data to a 2D array with one row and two columns
    input_data=input_data.reshape(1, -1)
    
    # predict salary based on both yoe and edu_level
    y_pred = model.predict(input_data)
    st.write(f"your salary is must be around {y_pred[0]:,.2f}")

