import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.server.api:app", reload=True)