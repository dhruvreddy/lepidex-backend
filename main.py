from fastapi import FastAPI

from routers import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "ping": "pong"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)