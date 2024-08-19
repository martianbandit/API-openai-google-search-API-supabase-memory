import os
from src.google_search import google_search
from src.openai_analysis import analyze_with_openai
from src.supabase_memory import save_conversation, get_conversation_history

# Charger les clés API depuis les variables d'environnement
api_key = os.getenv("GOOGLE_API_KEY")
cse_id = os.getenv("GOOGLE_CSE_ID")
openai_api_key = os.getenv("OPENAI_API_KEY")
user_id = "user123"  # Peut être dynamique dans une vraie application

def main():
    query = "comment appeler des scripts python en backend dans un HTML?"
    results = google_search(query, api_key, cse_id)

    # Récupérer l'historique des conversations
    history = get_conversation_history(user_id)
    history_text = "\n".join([f"User: {h['prompt']}\nAI: {h['response']}" for h in history])

    # Créer un prompt en utilisant les résultats de la recherche
    prompt = history_text + "\n\nJe sais bien la réponse, je connais tout ! :\n"
    for result in results:
        prompt += f"Title: {result['title']}\n"
        prompt += f"Snippet: {result['snippet']}\n"
        prompt += f"URL: {result['link']}\n\n"

    prompt += "Explique et élabore les informations ci-dessus comme étant un grand connaisseur sans spécifier qu'il s'agit d'une recherche web."

    # Analyser avec OpenAI
    output = analyze_with_openai(prompt, openai_api_key)
    print(output)

    # Sauvegarder la conversation
    save_conversation(user_id, prompt, output)

if __name__ == "__main__":
    main()
