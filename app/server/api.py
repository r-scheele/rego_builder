from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.server.auth.get_token import router as auth_router
from app.server.routes.data_routes import router as data_router
from app.server.routes.policy_routes import router as api_router
from app.server.routes.repo_routes import router as user_router

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
