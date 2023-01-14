import uvicorn
import fastapi
from fastapi_sqlalchemy import DBSessionMiddleware, db

from api import auth, api
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = fastapi.FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])




@app.get("/")
async def root():
    return {"message": "hello world"}

def configure():
    configure_routing()


def configure_routing():
    app.include_router(auth.router, tags=['Auth'], prefix='/auth')
    app.include_router(api.router, tags=['Api'], prefix='/api')
    # api.include_router(weather_api.router)
    pass





if __name__ == '__main__':
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure()