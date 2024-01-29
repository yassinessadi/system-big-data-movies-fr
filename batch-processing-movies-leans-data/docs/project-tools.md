**GitHub README: Setting Up MovieCredits Database Project**

**Requirements:**

- `Airflow`
- `SQL Server`
- `Python`
- `WSL` (`Windows` Subsystem for `Linux`)
- `pyodbc`
- `pandas`
- The Movie Database (`TMDb`) API
- `Lucidchart` for `Data Modeling`
- `Jupyter Notebook`

**Installation:**

1. Airflow: Install using.

```bash
    # airflow default port is:
    # http://localhost:8080/home

    export AIRFLOW_HOME=~/airflowpip3 install apache-airflowpip3 install typing_extensions
    # initialize the database
    airflow db init

    # start the web server, default port is 8080
    airflow webserver -p 8080
    # start the scheduler. I recommend opening up a separate terminal #window for this step
    airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page
```

2. `SQL` Server: Install and configure SQL Server.
3. `Python`: Ensure Python is installed (version 3.x recommended).
4. `WSL`: Set up Windows Subsystem for Linux.
5. `pyodbc`: Install using :

```bash
    pip install pyodbc
```

6. `pandas`: Install using:

```bash
    pip install pandas
```

7. The Movie Database (`TMDb`) API: Obtain API key from TMDb `https://www.themoviedb.org/settings/api`.
   _Note: Replace placeholder text with actual details, and ensure to set up necessary credentials/API keys._

8. `Lucidchart`: Sign up for Lucidchart account `https://lucid.app/lucidchart`.
9. `Jupyter Notebook`: Install using VSCode.
