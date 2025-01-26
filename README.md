# Twitter API Data Extraction, Transformation, Load

### 1. Create a Virtual Environment 🛠️
- Start by creating a virtual environment for Apache Airflow to isolate its dependencies from other projects.
```bash
python -m venv airflow_venv
```
This creates a directory named airflow_venv in your current working directory

### 2. Activate the Virtual Environment 🧑‍💻
```bash
source airflow_venv/bin/activate
```

### 3. Install Apache Airflow 🚀
- Now, install Apache Airflow within the virtual environment using pip

```bash
pip install apache-airflow
```
This command installs Apache Airflow and its dependencies in the virtual environment, isolating it from the global Python environment.

### 4. Initialize the Database 🗄️
- Apache Airflow requires a database to track metadata. Initialize the database with the following command:

```bash
airflow db init
```

### 5. Create an Admin User 👨‍💻
- Create an admin user for the Airflow web UI

```bash
airflow users create \
    --username anowerhossain97 \
    --firstname Anower \
    --lastname Hossain \
    --role Admin \
    --email anower.hossain@example.com \
    --password admin
```

### 6. Start the Web Server 🌐
- The web server serves the Airflow UI, which you can access through your browser.

```bash
airflow webserver -p 8081
```
Starts the web server that runs Airflow’s UI, typically accessible at http://localhost:8081 

### 7. Start the Scheduler ⏲️
- The scheduler is responsible for triggering and running tasks in your DAGs.
```bash
airflow scheduler
```
It schedules and monitors your DAGs (Directed Acyclic Graphs). This service continuously checks for tasks that need to be executed.

### 8. Access the Web UI 🖥️
- After starting the webserver, open your browser and go to: http://localhost:8080

This allows you to access the Airflow UI where you can view your DAGs, task statuses, logs, and manage workflows.


# Extract Tweets from Twitter API
- Extract tweets based on a specific query using the Twitter API v2 and store the raw data temporarily. Obtain your Twitter API credentials (Bearer Token) from the Twitter Developer Portal.

Set Up Twitter API Credentials 🔑

## 📋 DAG Steps
Step 1: Create Twitter API Headers 📝

- The first step involves setting up the authentication headers needed to make requests to the Twitter API.
```python
def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
    }
```

Step 2: Fetch Tweets from the API 📡

- In this step, a request is sent to Twitter's search/recent API endpoint to fetch tweets related to a specific query. The response is captured and returned as JSON.
```python
def fetch_tweets(query, max_results=10):
    headers = create_headers(BEARER_TOKEN)
    params = {
        "query": f"{query} lang:en",
        "tweet.fields": "text,author_id,created_at, context_annotations",
        "max_results": max_results,
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
```


Step 3: Extract Tweets into a DataFrame 📊

- Once the tweets are fetched, this step converts the JSON response into a pandas DataFrame for easy data manipulation.

```python
def extract_tweets_to_dataframe(query, max_results=1):
    data = fetch_tweets(query, max_results)
    if data and "data" in data:
        tweets = data["data"]
        df = pd.DataFrame(tweets)
        print("Fetched Tweets:")
        print(df.head())
        return df
    else:
        print("No tweets found or error occurred.")
        return None
```


Step 4: Save DataFrame to CSV 💾

- This step saves the extracted tweets into a CSV file for future analysis.
```python
def save_to_csv(dataframe, filename):
    if dataframe is not None:
        dataframe.to_csv(filename, index=False)
        print(f"Tweets saved to {filename}")
    else:
        print("No data to save.")
```

# 🐳 Airflow DAG Implementation
