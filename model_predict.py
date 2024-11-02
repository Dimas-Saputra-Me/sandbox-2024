import streamlit as st
import tensorflow as tf
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification

@st.cache_data
def predict(text):
    if "model" not in st.session_state.keys():
        save_directory = "./model"
        st.session_state["tokenizer"] = DistilBertTokenizer.from_pretrained(save_directory)
        st.session_state["model"] = TFDistilBertForSequenceClassification.from_pretrained(save_directory)
    
    model = st.session_state["model"]
    tokenizer = st.session_state["tokenizer"]

    # Tokenize
    predict_input = tokenizer.encode(text,
                                    truncation=True,
                                    padding=True,
                                    return_tensors="tf")

    # Forward to model
    output = model(predict_input)

    # TODO: CHANGE TO SOFTMAX LATER
    # Get prediction value
    prediction_value = tf.argmax(output.logits, axis=1).numpy()[0]
    
    # Classify int value to text
    prediction_label = "ERROR! unkown class" # set error default label
    if prediction_value == 0:
        prediction_label = "Data Scientist"
    elif prediction_value == 1:
        prediction_label = "UI/UX"
    elif prediction_value == 2:
        prediction_label = "Web"
    else:
        prediction_label = "ERROR! unkown class"
        
    return prediction_label


