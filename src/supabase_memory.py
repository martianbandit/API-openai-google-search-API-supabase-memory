from supabase import create_client, Client
from datetime import datetime, timezone
import os

def create_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

def save_conversation(user_id, prompt, response):
    supabase: Client = create_supabase_client()
    data = {
        "user_id": user_id,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    supabase.table("Conversations").insert(data).execute()

def get_user_data_from_supabase(user_id, supabase_client):
    try:
        response = supabase_client.table('users').select('*').eq('id', user_id).execute()
        return response.data
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des données utilisateur: {e}")
        return None

