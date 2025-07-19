import streamlit as st
import openai
import os

st.title("AI Code Assistant")

# Step 1: API Key input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Step 2: Ask prompt
prompt = st.text_area("What do you want help with?", height=150)

if st.button("Generate Code"):
    if not api_key:
        st.warning("Please enter your OpenAI API Key.")
    elif not prompt:
        st.warning("Please type a prompt.")
    else:
        with st.spinner("Generating..."):
            try:
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                code = response.choices[0].message.content
                st.code(code, language='python')
            except Exception as e:
                st.error(f"Error: {e}")
