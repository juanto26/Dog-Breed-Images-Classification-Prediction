import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Dog Breed EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
     st.title('Dog Breed Prediction')
     st.subheader('EDA to analyze Dog Breed')
     st.image('https://img.freepik.com/free-photo/beagle-tricolor-puppy-is-posing-cute-white-braun-black-doggy-pet-is-sitting-blue-background-looks-attented-sad-studio-photoshot-concept-motion-movement-action-negative-space_155003-33947.jpg',
              caption='Dog Breed')
     st.write('This page was created by Evan Juanto')
     st.markdown('---')

     st.write('# 1. Visualisasi Breed Beagle')
     st.image('output.png', caption='Visualisasi Breed Beagle', use_column_width=True)
     st.write('# 2. Visualisasi Breed Boxer')
     st.image('output1.png', caption='Visualisasi Breed Boxer', use_column_width=True)
     st.write('# 3. Visualisasi Breed Bulldog')
     st.image('output2.png', caption='Visualisasi Breed Bulldog', use_column_width=True)
     st.write('# 4. Visualisasi Breed Dachshund')
     st.image('o3.png', caption='Visualisasi Breed Dachshund', use_column_width=True)
     st.write('# 5. Visualisasi Breed German Shepherd')
     st.image('o4.png', caption='Visualisasi Breed German Shepherd', use_column_width=True)
     st.write('# 6. Visualisasi Breed Golden Retriever')
     st.image('o6.png', caption='Visualisasi Breed Golden Retriever', use_column_width=True)
     st.write('# 7. Visualisasi Breed Labrador Retriever')
     st.image('o7.png', caption='Visualisasi Breed Labrador Retriever', use_column_width=True)
     st.write('# 8. Visualisasi Breed Poodle')
     st.image('o8.png', caption='Visualisasi Breed Poodle', use_column_width=True)
     st.write('# 9. Visualisasi Breed Rottweiler')
     st.image('o9.png', caption='Visualisasi Breed Rottweiler', use_column_width=True)
     st.write('# 10. Visualisasi Breed Yorkshire Terrier')
     st.image('o10.png', caption='Visualisasi Breed Yorkshire Terrier', use_column_width=True)

if __name__ == "__main__":
    run()
     