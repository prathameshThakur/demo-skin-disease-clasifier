import streamlit as st
from PIL import Image

st.info("This an demo application, some element's wont work!")
st.title("AI BASED SKIN DISEASES CLASSIFIER")
image = Image.open('tenor.png')
st.image(image, caption='Is this disease cancerous!?')

st.sidebar.title('Tuning space!👨‍⚕️🦠🤖')
st.sidebar.slider('Zoom the image',0,100)
st.sidebar.selectbox('Chose model',['m1','m2','m3'])
st.sidebar.button('Show Infected areas')
st.file_uploader("Upload the image of infected skin",type=['png','jpg','jpeg'])
rep = st.button('Generate Report', key='rep')
if rep:
    st.success("type of disease:xyz\n\naccuracy: 45234\n\ncancerous (yes/no): no\n\nConsulting needed : yes")