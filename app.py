import streamlit as st
import openai

st.set_page_config(page_title="Code Assistant", layout="wide")

st.title("🧠 Code Assistant App")

# Input for API key
api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

# Input for user prompt
prompt = st.text_area("💬 What do you want help with?")

# Button to generate code
if st.button("🚀 Generate Code"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not prompt:
        st.warning("Please enter a prompt to generate code.")
    else:
        try:
            # Use OpenAI client from new SDK
            client = openai.OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response.choices[0].message.content
            st.code(answer, language='python')

        except Exception as e:
            st.error(f"❌ Error: {e}")
