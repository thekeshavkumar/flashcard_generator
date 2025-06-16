import streamlit as st
import openai
import pandas as pd
import json
from dotenv import load_dotenv
import os

from generator import generate_flashcards
from utils import extract_text_from_file

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Flashcard Generator", layout="wide")

def main():
    st.title("🧠 LLM-Powered Flashcard Generator")

    # --- Input Section ---
    st.header("📥 Input Educational Content")
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    text_input = st.text_area("Or paste educational content here:")
    subject = st.selectbox("Select Subject", ["Biology", "Computer Science", "Mathematics", "History", "General"])

    content = ""
    if uploaded_file:
        content = extract_text_from_file(uploaded_file)
    elif text_input:
        content = text_input

    if st.button("🚀 Generate Flashcards"):
        if content:
            with st.spinner("Generating flashcards..."):
                flashcards = generate_flashcards(content, subject)
                st.session_state["flashcards"] = flashcards
                st.success(f"{len(flashcards)} flashcards generated!")
        else:
            st.error("Please provide some content.")

    # --- Flashcard Display ---
    if "flashcards" in st.session_state:
        st.header("📚 Flashcards")
        for i, card in enumerate(st.session_state["flashcards"]):
            with st.expander(f"Flashcard {i + 1}"):
                q = st.text_area(f"Question {i + 1}", card["question"], key=f"q_{i}")
                a = st.text_area(f"Answer {i + 1}", card["answer"], key=f"a_{i}")
                st.session_state["flashcards"][i] = {"question": q, "answer": a}

        # --- Export Options ---
        st.subheader("📤 Export Flashcards")
        export_format = st.selectbox("Select Format", ["JSON", "CSV", "TXT"])
        if st.button("Export"):
            export_flashcards(st.session_state["flashcards"], export_format)

def export_flashcards(flashcards, format):
    if format == "JSON":
        with open("flashcards.json", "w", encoding="utf-8") as f:
            json.dump(flashcards, f, indent=2)
        st.success("Exported to flashcards.json")

    elif format == "CSV":
        df = pd.DataFrame(flashcards)
        df.to_csv("flashcards.csv", index=False)
        st.success("Exported to flashcards.csv")

    elif format == "TXT":
        with open("flashcards.txt", "w", encoding="utf-8") as f:
            for card in flashcards:
                f.write(f"Q: {card['question']}\nA: {card['answer']}\n\n")
        st.success("Exported to flashcards.txt")


if __name__ == "__main__":
    main()
