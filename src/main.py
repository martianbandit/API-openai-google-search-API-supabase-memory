import os
import sys
import logging

from google_search import google_search
from openai_analysis import analyze_with_openai
from supabase_memory import save_conversation, get_conversation_history

# Charger les clés API depuis les variables d'environnement
api_key = os.getenv("GOOGLE_API_KEY")
cse_id = os.getenv("GOOGLE_CSE_ID")
openai_api_key = os.getenv("OPENAI_API_KEY")
 # Peut être dynamique dans une vraie application

print("Variables d'environnement chargées.")

def main():
    print("Fonction main() démarrée.")
    
    query = "comment appeler des scripts python en backend dans un HTML?"
    print(f"Query: {query}")
    
    results = google_search(query, api_key, cse_id)
    print(f"Résultats de la recherche Google obtenus. Nombre de résultats: {len(results)}")

    # Récupérer l'historique des conversations
    history = get_conversation_history(user_id)
    print(f"Historique des conversations récupéré. Nombre d'entrées: {len(history)}")
    
    history_text = "\n".join([f"User: {h['prompt']}\nAI: {h['response']}" for h in history])

    # Créer un prompt en utilisant les résultats de la recherche
    prompt = history_text + "\n\nJe sais bien la réponse, je connais tout ! :\n"
    for result in results:
        prompt += f"Title: {result['title']}\n"
        prompt += f"Snippet: {result['snippet']}\n"
        prompt += f"URL: {result['link']}\n\n"

    prompt += "Explique et élabore les informations ci-dessus comme étant un grand connaisseur sans spécifier qu'il s'agit d'une recherche web."
    
    print("Prompt créé pour l'analyse OpenAI.")

    # Analyser avec OpenAI
    output = analyze_with_openai(prompt, openai_api_key)
    print("Analyse OpenAI terminée.")
    print("Résultat de l'analyse:")
    print(output)

    # Sauvegarder la conversation
    save_conversation(user_id, prompt, output)
    print("Conversation sauvegardée dans la base de données.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print("Démarrage de l'application...")
        main()
        print("Application terminée avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        logging.error(f"Une erreur s'est produite : {e}")
        sys.exit(1)