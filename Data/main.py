import pickle
with open('model.pickle','rb') as file:
    model = pickle.load(file)
    
    
    
import streamlit as st
yoe = st.text_input('Years of Exprience : ')

if st.button('Submit'):
    y_pred = model.predict([[int(yoe)]])
    st.write(f'Your Salary must be around {y_pred[0],2}')