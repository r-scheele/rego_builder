import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.server.auth.authenticate import router as auth_router
from app.server.routes.data import router as data_router
from app.server.routes.policies import router as api_router
from app.server.routes.user import router as user_router
from app.config.config import settings


app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    title="Policy Management API",
    version="0.1.0",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(api_router)
app.include_router(user_router)
app.include_router(data_router)
