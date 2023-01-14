# Shpping-cart-fastapi

This is a RESTful API application than serves a stateless shopping cart. it includes all relevant api's to manage producats and personal shopping carts and Authorize clients with JWT.

### 1. Project Structure


```
fastapi-project
├── alembic/
|
├── api
│   ├── __init__.py
│   ├── api.py  
│   └── auth.py  
|
└── app
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── oauth2.py
│   └── utils.py
|
└── db
│   ├── models.py
│   └── schema.py
|
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── alembic.ini
```

1. Store all domain directories inside `fastapi-project` folder
   1. `api/api.py` - all the CRUD api's are there
   2. `api/auth.py` - all the JWT api's are there
   3. `app/config.py` - database configurations load there
   4. `app/database.py` - database session connecting for accessing to data and queries 
   5. `app/oauth2.py` - JWT settings and built-in methods implemented here
   6. `app/utils.py` - Password encription and decription implemented here
   7. `db/models.py` - database models implemented here
   8. `db/schema.py` - database schemas implemented here
   9. `main.py` - root of the project, which inits the FastAPI app
   10. `requirements.txt` - Project requirements
   11. `.env` - enviromental variables

### 2. Project Usage
```
python -m venv venv

\venv\Scripts\Acrivate

pip install -r requirements.txt

alembic init alembic

alembic revision --autogenerate -m "Migration"

alembic upgrade head
```


### 3. Project API'S



![API'S](https://github.com/horrhamid/Shpping-cart-fastapi/blob/main/ScreenShot.png)
