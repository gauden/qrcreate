import streamlit as st
import qrcode
from PIL import Image

# Function to determine the appropriate version based on URL length
def determine_version(url_length):
    if url_length <= 25:
        return 1
    elif url_length <= 47:
        return 2
    elif url_length <= 77:
        return 3
    elif url_length <= 114:
        return 4
    elif url_length <= 154:
        return 5
    elif url_length <= 195:
        return 6
    elif url_length <= 224:
        return 7
    elif url_length <= 279:
        return 8
    else:
        return 9

# Function to create and display QR code inline
def generate_qr_code(url, box_size, border, image_size):
    # Determine the appropriate version based on URL length
    version = determine_version(len(url))
    
    # Create a QR code object
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white').convert('RGB')
    
    # Resize the image
    img = img.resize(image_size)
    
    return img

# Streamlit app
st.title("QR Code Generator")

# Sidebar for input fields and GitHub link
st.sidebar.title("Settings")
url = st.sidebar.text_input("Enter the URL:", "https://www.example.com")
box_size = st.sidebar.number_input("Box Size:", min_value=1, value=10)
border = st.sidebar.number_input("Border Size:", min_value=1, value=4)
width = st.sidebar.number_input("Image Width:", min_value=50, value=300)
height = st.sidebar.number_input("Image Height:", min_value=50, value=300)

# Generate and display QR code
generate_button = st.sidebar.button("Generate QR Code")

if generate_button:
    image_size = (width, height)
    qr_image = generate_qr_code(url, box_size, border, image_size)
    st.image(qr_image, caption="Generated QR Code")
else:
    st.write("### Instructions")
    st.write("""
    To generate a QR code, enter the URL and adjust the settings in the sidebar on the left.
    - **URL**: The web address or string you want to encode.
    Optional additional parameters you may want to tweak:
    - **Box Size**: Size of each box in the QR code.
    - **Border Size**: Width of the border around the QR code.
    - **Image Width**: Width of the output image (in pixels).
    - **Image Height**: Height of the output image (in pixels).

    After setting the parameters, click the "Generate QR Code" button.
    """)
