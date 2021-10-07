# Python Postgres

## Instructions to create and populate the PostgresSQL database.

Hosting the MongoDB Community Server locally:

-   Download Postgres onto your machine and configure user details to:

        Username: `postgres`
        Password: `password`

-   Create database and name it 'store'

-   Create a python file named vars.py and populate it with:

        HOSTNAME = "localhost"
        DATABASE_NAME = "store"
        USERNAME = "postgres"
        PASSWORD = "password" // or whatever you set it to
        PORT = 5432 // default port used by postgres

-   Downloading the dependencies

        cd into the directory
        run 'pip install -r requirements.txt'
