import openai
import time
import re
import os
from openai import OpenAI
from openai import RateLimitError

def generate_flashcards(content, subject):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
Generate 3 flashcards from the content below.
Each flashcard should look like:

Q: What is the CPU?
A: The central processing unit of a computer.

Use only the following content:
\"\"\"
{content}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        raw_output = response.choices[0].message.content
        print("RAW GPT OUTPUT:")
        print(raw_output)

        # Return raw GPT output for debugging in the app
        return [{"question": "RAW", "answer": raw_output}]

    except Exception as e:
        print(f"Error: {e}")
        return [{"question": "error", "answer": str(e)}]
