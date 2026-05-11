import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process-lead"

st.set_page_config(
    page_title="AI Lead Qualification System",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Lead Qualification System")

st.markdown("""
This system:
- Classifies customer leads
- Generates AI-powered responses
- Stores results in database
""")

lead_message = st.text_area(
    "Enter Customer Lead Message",
    height=150,
    placeholder="Example: I want pricing details for your AI services..."
)

if st.button("Process Lead"):

    if not lead_message.strip():
        st.warning("Please enter a lead message.")
    else:

        with st.spinner("Processing lead..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "message": lead_message
                    }
                )

                data = response.json()

                st.success("Lead Processed Successfully")

                st.subheader("Lead Category")
                st.code(data["category"])

                st.subheader("AI Response")
                st.write(data["response"])

                st.subheader("Status")
                st.code(data["status"])

            except Exception as e:

                st.error(f"Error: {str(e)}")
                