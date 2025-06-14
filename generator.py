import openai

def generate_flashcards(content, subject):
    openai.api_key = "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"
    
    prompt = f"Generate 10-15 question-answer flashcards based on the following content in the subject of {subject}:\n\n{content}\n\nFormat the output as JSON."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    flashcards = response['choices'][0]['message']['content']
    return json.loads(flashcards)
