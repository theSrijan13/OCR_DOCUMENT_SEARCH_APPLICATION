import easyocr
from PIL import Image
import streamlit as st
import numpy as np

# OCR Function with improved image handling
def ocr_image(image):
    # Initialize easyocr Reader with support for English ('en') and Hindi ('hi')
    reader = easyocr.Reader(['en', 'hi'])
    
    # Perform OCR on the image (must convert to numpy array or bytes)
    result = reader.readtext(np.array(image), detail=0)  # Convert image to numpy array
    
    return result

# Streamlit Web App for OCR and Image Upload
def main():
    st.title("OCR Web App for English and Hindi Text")
    
    # File uploader to allow users to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Load the uploaded image using Pillow
        image = Image.open(uploaded_file)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Convert the image to RGB mode
        image = image.convert("RGB")
        
        # Perform OCR on the image
        extracted_text = ocr_image(image)

        # Display the extracted text
        if extracted_text:
            st.write("### Extracted Text:")
            for i, text in enumerate(extracted_text):
                st.write(f"{i+1}: {text}")
        else:
            st.write("No text could be extracted from the image.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
