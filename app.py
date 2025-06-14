import streamlit as st
import json
from generator import generate_flashcards
from utils import extract_text_from_file

def main():
    st.title("LLM-Powered Flashcard Generator")
    
    # Input system
    st.header("Input Educational Content")
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    text_input = st.text_area("Or enter text directly here:")
    
    subject = st.selectbox("Select Subject", ["Biology", "Computer Science", "Mathematics", "History"])
    
    if uploaded_file is not None:
        content = extract_text_from_file(uploaded_file)
    else:
        content = text_input
    
    if st.button("Generate Flashcards"):
        if content:
            flashcards = generate_flashcards(content, subject)
            st.session_state.flashcards = flashcards
            st.success("Flashcards generated successfully!")
        else:
            st.error("Please provide some content.")
    
    # Display flashcards
    if 'flashcards' in st.session_state:
        st.header("Generated Flashcards")
        for idx, card in enumerate(st.session_state.flashcards):
            st.subheader(f"Flashcard {idx + 1}")
            st.write(f"**Question:** {card['question']}")
            st.write(f"**Answer:** {card['answer']}")
            if st.button(f"Edit Flashcard {idx + 1}"):
                new_question = st.text_input("Edit Question", value=card['question'])
                new_answer = st.text_input("Edit Answer", value=card['answer'])
                st.session_state.flashcards[idx] = {"question": new_question, "answer": new_answer}
        
        if st.button("Export Flashcards"):
            export_format = st.selectbox("Select Export Format", ["JSON", "CSV", "TXT"])
            export_flashcards(st.session_state.flashcards, export_format)

def export_flashcards(flashcards, format):
    if format == "JSON":
        with open("flashcards.json", "w") as f:
            json.dump(flashcards, f)
        st.success("Flashcards exported as flashcards.json")
    elif format == "CSV":
        import pandas as pd
        df = pd.DataFrame(flashcards)
        df.to_csv("flashcards.csv", index=False)
        st.success("Flashcards exported as flashcards.csv")
    elif format == "TXT":
        with open("flashcards.txt", "w") as f:
            for card in flashcards:
                f.write(f"Q: {card['question']}\nA: {card['answer']}\n\n")
        st.success("Flashcards exported as flashcards.txt")

if __name__ == "__main__":
    main()
