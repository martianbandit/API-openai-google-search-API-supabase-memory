import requests

def google_search(query, api_key, cse_id, num_results=2):
    try:
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}&num={num_results}"
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        results = response.json()
        return results.get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la recherche Google: {e}")
        return []