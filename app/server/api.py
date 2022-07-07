from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.server.auth.authenticate import router as auth_router
from app.server.policies import router as api_router
from app.server.user import router as user_router

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
app.include_router(api_router)
app.include_router(user_router)
