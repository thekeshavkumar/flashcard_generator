# 🧠 LLM-Powered Flashcard Generator

A Streamlit web app that uses OpenAI's GPT to generate question-answer flashcards from text or PDF content.

## 🚀 Features

- Upload `.pdf` or `.txt` or paste content
- Flashcards generated using OpenAI GPT-3.5
- Edit flashcards in-app
- Export to JSON, CSV, TXT

## 📦 Installation

```bash
git clone <(https://github.com/thekeshavkumar/flashcard_generator)>
cd flashcard_generator
pip install -r requirements.txt
```

## 🔑 Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=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
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📤 Output Example

```json
[
  {
    "question": "What is the function of mitochondria?",
    "answer": "It converts chemical energy into ATP."
  }
]
```

## 📁 Project Structure

```
flashcard_generator/
├── app.py
├── generator.py
├── utils.py
├── .env
├── requirements.txt
└── README.md
```
