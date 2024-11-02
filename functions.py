import streamlit as st
import base64
#------- OCR ------------
import pdf2image
import pytesseract

@st.cache_data
def images_to_txt(path, language):
    images = pdf2image.convert_from_bytes(path)
    all_text = []
    for i in images:
        pil_im = i
        custom_config = f'-l {language} --oem 3 --psm 6'
        text = pytesseract.image_to_string(pil_im, config=custom_config)
        all_text.append(text)
    return all_text, len(all_text)

def displayPDF(file):
  # Opening file from file path
  # with open(file, "rb") as f:
  base64_pdf = base64.b64encode(file).decode('utf-8')

  # Embedding PDF in HTML
  pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
  # Displaying File
  st.markdown(pdf_display, unsafe_allow_html=True)