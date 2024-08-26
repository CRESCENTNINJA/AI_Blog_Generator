import streamlit as st
import os
import google.generativeai as genai
from apikey import gem_api_key


# Configuration of the Google GenAI API
genai.configure(api_key=gem_api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Set app to wide mode
st.set_page_config(layout="wide")

# Title of our app
st.title("My AI Blog Companion")

# Create a subheader
st.subheader("This is my AI Blog Companion App")

# Sidebar for user input
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter Details of the Blog that you want to generate.")

    # Blog Title
    blog_title = st.text_input("Blog Title")

    # Keywords input
    keywords = st.text_area("Keywords (comma-separated)")

    # Number of words
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=250)

    # Number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

# Create the model instance outside the sidebar, so it doesn't recreate it with each change
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Initialize chat session
chat_session = model.start_chat(
    history=[]
)

# Generate response on submit button click
if st.button("Generate Blog"):
    # Prepare the system instruction
    system_instruction = (
        f"Generate an engaging blog post, with a constant tone throughout. "
        f"The blog should contain {num_words} words. The blog should be relevant to the title given: "
        f"{blog_title}, and the keywords: {keywords}. In the end, generate a random fun fact."
    )

    # Send the message to the chat session
    chat_session.send_message(system_instruction)
    response = model.generate_content(f"Generate an engaging blog post, with a constant tone throughout. "
        f"The blog should contain {num_words} words. The blog should be relevant to the title given: "
        f"{blog_title}, and the keywords: {keywords}. In the end, generate a random fun fact.")



    # Display image and response
    st.write(response.text)





