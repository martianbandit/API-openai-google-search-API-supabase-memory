from supabase import create_client, Client
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
        "timestamp": datetime.utcnow().isoformat()
    }
    supabase.table("Conversations").insert(data).execute()

def get_conversation_history(user_id, limit=5):
    supabase: Client = create_supabase_client()
    response = supabase.table("Conversations").select("*").eq("user_id", user_id).order("timestamp", desc=True).limit(limit).execute()
    return response.data
