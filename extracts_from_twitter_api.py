import requests
import pandas as pd
import os

# Load your Twitter API Bearer Token (use environment variables for security)
BEARER_TOKEN = "AAAAAAAAAAAAAAAACq4wwEAAAAAXQUGSegRTZePfZ3RL9Vdm5B%2Bjpk%3DQX2ODtnbTDUG0ap4rwYo8ZDFmNfRSUdEoeXxpBhOSnFSY5w89A"  # Replace with your regenerated Bearer Token

# Define the Twitter API endpoint for recent tweet search
SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

# Function to create headers for authorization
def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
    }

# Function to make a request to the Twitter API
def fetch_tweets(query, max_results=10):
    headers = create_headers(BEARER_TOKEN)
    params = {
        "query": query,
        "tweet.fields": "text,author_id,created_at",  # Customize fields as needed
        "max_results": max_results,  # Max: 100
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting for 15 minutes...")
        time.sleep(15 * 60)  # Wait for 15 minutes
        return fetch_tweets(query, max_results)
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Fetch tweets and save to a DataFrame
def extract_tweets_to_dataframe(query, max_results=10):
    data = fetch_tweets(query, max_results)
    if data and "data" in data:
        tweets = data["data"]
        # Convert to DataFrame
        df = pd.DataFrame(tweets)
        print("Fetched Tweets:")
        print(df.head())
        return df
    else:
        print("No tweets found or error occurred.")
        return None

# Save DataFrame to a CSV file
def save_to_csv(dataframe, filename):
    if dataframe is not None:
        dataframe.to_csv(filename, index=False)
        print(f"Tweets saved to {filename}")
    else:
        print("No data to save.")

# Main execution
if __name__ == "__main__":
    query = "python"  # Replace with your search term
    max_results = 10  # Number of tweets to fetch
    filename = "tweets.csv"  # Output file

    # Fetch tweets and save them
    tweets_df = extract_tweets_to_dataframe(query, max_results)
    save_to_csv(tweets_df, filename)
