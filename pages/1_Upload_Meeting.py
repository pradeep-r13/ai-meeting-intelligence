import streamlit as st

from agents.decision_agent import extract_decisions

st.title("Upload Meeting")

uploaded_file = st.file_uploader(
    "Upload Transcript",
    type=["txt"]
)

if uploaded_file:

    transcript = uploaded_file.read().decode()

    st.success("Meeting Uploaded")

    with st.spinner("Analyzing Meeting..."):

        decisions = extract_decisions(transcript)

    st.subheader("Extracted Decisions")

    st.json(decisions)