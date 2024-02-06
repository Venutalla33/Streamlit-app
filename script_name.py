import streamlit as st
from PIL import Image

#Importing Libraries and Defining the Conversion Function
def convert_image(image_path, new_format):
    with Image.open(image_path) as img:

        new_name =image_path.name.split('.')[0] + '.' + new_format
        final_path = r'C:\Users\ACER\Pictures'+new_name

        img = img.convert('RGB')

        st.subheader(final_path)
        img.save(final_path)
        st.success('Image Saved at ' + final_path)

#Creating the Streamlit App
st.title('Image Converter')
# File Uploader for Image
image_path = st.file_uploader('Upload your image', type=['png', 'jpg', 'jpeg'])

# Format Selection Dropdown
new_format = st.selectbox('Select the output format', ['png', 'jpeg', 'jpg'])

# Conversion Button
if st.button('Convert'):
    if image_path is not None:
        convert_image(image_path, new_format)
    else:
        st.error('Please upload the image file')
