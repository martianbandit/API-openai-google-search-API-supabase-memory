import openai

def analyze_with_openai(prompt, openai_api_key):
    try:
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000
        )
        return response['choices'][0]['message']['content']
    except openai.OpenAIError as e:
        print(f"Erreur lors de l'analyse avec OpenAI: {e}")
        return ""
