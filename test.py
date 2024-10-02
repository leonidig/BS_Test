from os import getenv
import requests

def fetch_news(api_key, query='technology'):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'en', 
        'pageSize': 10,
        'sortBy': 'publishedAt'
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error while making the request:", response.status_code)
        print("Response from the server:", response.text)
        return []

    data = response.json()
    return data.get('articles', [])

def main():
    api_key = getenv("api_key")
    news = fetch_news(api_key)
    if news:
        for i, article in enumerate(news, 1):
            print(f"{i}. {article['title']}\n   {article['url']}\n")
    else:
        print("No news found.")

if __name__ == "__main__":
    main()
