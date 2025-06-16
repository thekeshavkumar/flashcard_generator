# 🧠 LLM-Powered Flashcard Generator

A Streamlit web app that uses OpenAI's GPT to generate question-answer flashcards from text or PDF content.

## 🚀 Features

- Upload `.pdf` or `.txt` or paste content
- Flashcards generated using OpenAI GPT-3.5
- Edit flashcards in-app
- Export to JSON, CSV, TXT

## 📦 Installation

```bash
git clone <[repo_url](https://github.com/thekeshavkumar/flashcard_generator)>
cd flashcard_generator
pip install -r requirements.txt
```

## 🔑 Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
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
