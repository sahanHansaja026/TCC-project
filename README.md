# download postgresql
-------------------------------------------------------
```bash
https://www.postgresql.org/download/
```

# download pgadmin
``` bash
https://www.pgadmin.org/download/
```

# create database connection
--------------------------------------------------------
go to the 
backend > database.py

```bash
DATABASE_URL = "postgresql://<username>:<password>@<host>:<port>/<database_name>"
```
replace with your deatails

 DATABASE_URL:
- postgresql:        The database dialect/driver
- postgres:          Username
- 123:               Password
- localhost:         Host (127.0.0.1)
- 5432:              Default PostgreSQL port
- test_fastapi_backend: Name of the database


# backend run
--------------------------------------------------------
```bash
cd backend
```

```bash
Remove-Item -Recurse -Force .\venv
```

```bash
python -m venv venv
```

```bash
.\venv\Scripts\Activate
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn main:app --reload

```
# client (front end) run
--------------------------------------------------------
```bash
cd client
```

```bash
npm i
```
```bash
npm run dev
```
