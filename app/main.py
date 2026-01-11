from fastapi import FastAPI
from app.routers import auth_routes, meeting_routes

app = FastAPI(title="Voice AI Assistant API")

@app.get("/")
def health():
    return {"status": "ok", "message": "Voice AI API is running"}


app.include_router(auth_routes.router)
app.include_router(meeting_routes.router)
