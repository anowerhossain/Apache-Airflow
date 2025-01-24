# Apache-Airflow

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
- After starting the webserver, open your browser and go to:
  
-- http://localhost:8080

This allows you to access the Airflow UI where you can view your DAGs, task statuses, logs, and manage workflows.
