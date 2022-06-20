from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from app.server.auth.authenticate import router as auth_router
from app.server.auth.authorize import TokenBearer

from app.server.routes import router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(router)

