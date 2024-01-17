# frontend.py
import streamlit as st
import requests

# Change the URL based on where your Flask app is running
BACKEND_URL = 'http://localhost:5000'

st.title('Image Similarity Search')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Upload the image to the backend
    upload_response = requests.post(f'{BACKEND_URL}/upload', files={'file': uploaded_file})

    if upload_response.status_code == 200:
        st.success('Image uploaded successfully!')
    else:
        st.error(f'Error uploading image: {upload_response.json()["error"]}')

    # Find similar images
    find_similar_response = requests.post(f'{BACKEND_URL}/find_similar', files={'file': uploaded_file})

    if find_similar_response.status_code == 200:
        similar_images = find_similar_response.json()['similar_images']
        st.write("Similar Images:")
        for img_url in similar_images:
            st.image(img_url, use_column_width=True)
    else:
        st.error(f'Error finding similar images: {find_similar_response.json()["error"]}')
